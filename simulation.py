import random, sys
from person import Person
from logger import Logger
from virus import Virus

class Simulation:
    def __init__(self, virus, population_size, vaccination_rate, initial_infected=1):
        """
        Initializes the simulation with parameters.
        """
        print("Starting simulation setup...")
        self.logger = Logger("simulation_log.txt")
        self.virus = virus
        self.population_size = population_size
        self.vaccination_rate = vaccination_rate
        self.initial_infected = initial_infected
        self.infected_count = initial_infected
        self.population = self._generate_population()
        self.newly_infected = []

        print(f"Simulation setup complete. Initial infected count: {self.infected_count}")
        self.logger.write_metadata(
            population_size, vaccination_rate, virus.name, virus.mortality_rate, virus.reproduction_rate  # <-- Updated here
        )

    def _generate_population(self):
        """
        Creates the population with initial infection and vaccination status.
        """
        population = []
        for i in range(self.population_size):
            if i < self.initial_infected:
                population.append(Person(i, vaccinated=False, infection=self.virus))
                self.infected_count += 1
            else:
                vaccinated = random.random() < self.vaccination_rate
                population.append(Person(i, vaccinated=vaccinated))
        return population

    def _should_continue(self):
        """
        Checks whether the simulation should continue running.
        """
        living_people = [p for p in self.population if p.is_alive]
        if not living_people or all(p.vaccinated for p in living_people):
            return False
        return True

    def time_step(self):
        """
        Runs a single timestep of the simulation, processing infection and survival.
        """
        for person in self.population:
            if person.is_alive and person.infection:
                interactions = 0
                while interactions < 100:
                    other_person = random.choice(self.population)
                    if other_person.is_alive and other_person != person:
                        self._interact(person, other_person)
                        interactions += 1
                person.check_for_death()
        self._infect_newcomers()

    def run(self):
        """
        Starts the simulation and runs it until termination.
        """
        print("Simulation running...")
        step_counter = 0
        while self._should_continue():
            step_counter += 1
            self.time_step()

            alive_count = len([p for p in self.population if p.is_alive])
            dead_count = self.population_size - alive_count
            self.logger.log_infection_status(step_counter, alive_count, dead_count)

        survivors = len([p for p in self.population if p.is_alive])
        vaccinated_survivors = sum([1 for p in self.population if p.is_alive and p.vaccinated])
        fatalities = self.population_size - survivors
        self.logger.log_summary(step_counter, self.population_size, survivors, fatalities, vaccinated_survivors)
        self.logger.log_total_infected(self.infected_count)

        clear_log = input("Clear the log file after this simulation? (y/n): ")
        if clear_log.lower() == 'y':
            with open(self.logger.file_name, 'w') as file:
                file.write("")  # Clears the log file content
            print(f"Log file '{self.logger.file_name}' cleared.")
        else:
            print("Log file not cleared.")

    def _interact(self, infected, other):
        """
        Handles interactions between an infected and a non-infected person.
        """
        if other.vaccinated or other.infection:
            return
        if random.random() < self.virus.reproduction_rate:
            self.newly_infected.append(other)
            self.infected_count += 1

    def _infect_newcomers(self):
        """
        Infects people in the 'newly_infected' list.
        """
        for person in self.newly_infected:
            person.infection = self.virus
        self.newly_infected.clear()

if __name__ == "__main__":
    if len(sys.argv) != 7:
        print("Usage: python3 simulation.py <population_size> <vaccination_percentage> <virus_name> <repro_rate> <mortality_rate> <initial_infected>")
        sys.exit(1)

    pop_size = int(sys.argv[1])
    vacc_percentage = float(sys.argv[2])
    virus_name = sys.argv[3]
    repro_rate = float(sys.argv[4])
    mortality_rate = float(sys.argv[5])
    initial_infected = int(sys.argv[6])

    virus = Virus(virus_name, repro_rate, mortality_rate)
    sim = Simulation(virus, pop_size, vacc_percentage, initial_infected)
    sim.run()
