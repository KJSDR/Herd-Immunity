import random
from person import Individual
from logger import SimulationLogger
from virus import Virus

class PandemicSimulation:
    """Handles the entire pandemic simulation process."""

    def __init__(self, population_size, vaccination_rate, virus, initial_infected=1):
        """Initializes the simulation parameters and creates the population."""
        self.logger = SimulationLogger('simulation_log.txt')
        self.virus = virus
        self.population_size = population_size
        self.vaccination_rate = vaccination_rate
        self.initial_infected = initial_infected
        self.population = self._create_population()
        self.new_infections = []
        self.total_interactions = 0

        self.logger.log_metadata(population_size, vaccination_rate, virus.name, virus.mortality_rate, virus.repro_rate, initial_infected)

    def _create_population(self):
        """Generates the population with a mix of vaccinated, infected, and healthy individuals."""
        population = []
        for i in range(self.population_size):
            if i < self.initial_infected:
                person = Individual(i, False, self.virus)
                population.append(person)
            elif i < self.population_size * self.vaccination_rate:
                person = Individual(i, True)
                population.append(person)
            else:
                person = Individual(i, False)
                population.append(person)
        return population

    def _should_continue(self):
        """Checks if the simulation should continue based on the number of infected, alive people."""
        infected_alive = sum(1 for p in self.population if p.alive and p.infection)
        non_vaccinated_alive = sum(1 for p in self.population if p.alive and not p.vaccinated)
        return infected_alive > 0 and non_vaccinated_alive > 0

    def start(self):
        """Starts the simulation and runs it until it finishes."""
        step = 0
        while self._should_continue():
            step += 1
            self.run_step(step)

        living_count = sum(1 for p in self.population if p.alive)
        dead_count = len(self.population) - living_count
        vaccinated_count = sum(1 for p in self.population if p.vaccinated)
        self.logger.log_summary(living_count, dead_count, vaccinated_count, self.total_interactions)

    def run_step(self, step):
        """Simulates a single step (time unit) in the pandemic simulation."""
        interactions = 0
        fatalities = 0
        total_alive = len([p for p in self.population if p.alive])
        total_dead = len([p for p in self.population if not p.alive])
        vaccinated_count = sum(1 for p in self.population if p.vaccinated)

        for person in self.population:
            if person.infection:
                for _ in range(100):
                    other_person = random.choice(self.population)
                    interactions += 1
                    self.handle_interaction(person, other_person)

        new_infections = len(self.new_infections)
        self._apply_new_infections()
        self.logger.record_interactions(step, interactions, new_infections)

        for person in self.population:
            if person.infection and person.alive:
                if not person.survive_or_die():
                    fatalities += 1

        self.logger.record_survival_stats(step, len(self.population), fatalities, total_alive, total_dead, vaccinated_count)
        self.total_interactions += interactions

    def handle_interaction(self, infected, other_person):
        """Handles a single interaction between an infected person and a random individual."""
        if other_person.alive and not other_person.vaccinated and not other_person.infection:
            if random.random() < self.virus.repro_rate:
                self.new_infections.append(other_person)

    def _apply_new_infections(self):
        """Infects all newly infected individuals."""
        for person in self.new_infections:
            person.infection = self.virus
        self.new_infections.clear()

if __name__ == "__main__":
    virus_instance = Virus("CommonCold", 0.6, 0.1)
    sim = PandemicSimulation(1000, 0.2, virus_instance, initial_infected=10)
    sim.start()
