import random, sys
from person import Person
from logger import Logger
from virus import Virus


class Simulation(object):
    def __init__(self, virus, pop_size, vacc_percentage, initial_infected=1):
        # Create a Logger object and bind it to self.logger
        self.logger = Logger("simulation_log.txt")

        # Store the virus, population size, vaccination percentage, and initial infected count
        self.virus = virus
        self.pop_size = pop_size
        self.vacc_percentage = vacc_percentage
        self.initial_infected = initial_infected

        # Call self._create_population() and store the list in an attribute
        self.population = self._create_population()

        # Track newly infected individuals
        self.newly_infected = []

        # Log metadata to the file
        self.logger.write_metadata(
            pop_size=self.pop_size,
            vacc_percentage=self.vacc_percentage,
            virus_name=self.virus.name,
            mortality_rate=self.virus.mortality_rate,
            basic_repro_num=self.virus.repro_num,
        )

    def _create_population(self):
        # Create a list of people (Person instances)
        population = []

        # Create vaccinated and unvaccinated people based on the vaccination percentage
        for i in range(self.pop_size):
            is_vaccinated = random.random() < self.vacc_percentage
            person = Person(i + 1, is_vaccinated)  # Person's ID starts from 1
            population.append(person)

        # Infect the initial number of people
        infected_indices = random.sample(range(self.pop_size), self.initial_infected)
        for i in infected_indices:
            population[i].infection = self.virus

        return population

    def _simulation_should_continue(self):
        # Check if the simulation should continue: either people are alive or unvaccinated
        living_people = [person for person in self.population if person.is_alive]
        if not living_people:  # No one is alive
            return False

        # Check if there's at least one unvaccinated person who is alive
        unvaccinated_living = [person for person in living_people if not person.is_vaccinated]
        return len(unvaccinated_living) > 0

    def run(self):
        # Start the simulation and track the number of steps
        time_step_counter = 0
        should_continue = True

        while should_continue:
            time_step_counter += 1
            self.time_step()  # Run one time step
            should_continue = self._simulation_should_continue()

        # Log the final results when simulation completes
        living_count = sum(1 for person in self.population if person.is_alive)
        dead_count = self.pop_size - living_count
        vaccinated_count = sum(1 for person in self.population if person.is_vaccinated)

        self.logger.write_final_data(
            population_size=self.pop_size,
            living=living_count,
            dead=dead_count,
            vaccinated=vaccinated_count,
            steps=time_step_counter,
        )

    def time_step(self):
        # Simulate interactions between infected and non-infected people
        for person in self.population:
            if person.infection and person.is_alive:
                # If the person is infected, have them interact with 100 other people
                for _ in range(100):  # Each infected person interacts with 100 people
                    random_person = random.choice(self.population)
                    if random_person.is_alive:
                        self.interaction(person, random_person)

        # After all interactions, infect the newly infected people
        self._infect_newly_infected()

    def interaction(self, infected_person, random_person):
        # If random person is vaccinated, no infection occurs
        if random_person.is_vaccinated:
            return

        # If random person is already infected, no infection occurs
        if random_person.infection:
            return

        # If random person is healthy and unvaccinated, they may become infected
        infection_chance = random.random()
        if infection_chance < self.virus.repro_num:
            random_person.infection = self.virus
            self.newly_infected.append(random_person)
            self.logger.log_interactions(
                step_number=0,  # This will be handled by time_step
                number_of_interactions=1,
                number_of_new_infections=1,
            )

    def _infect_newly_infected(self):
        # At the end of each time step, infect all newly infected people
        for person in self.newly_infected:
            person.infection = self.virus
        # Reset the newly infected list for the next time step
        self.newly_infected.clear()

if __name__ == "__main__":
    # Test your simulation here
    virus_name = "Sniffles"
    repro_num = 0.5
    mortality_rate = 0.12
    virus = Virus(virus_name, repro_num, mortality_rate)

    # Set some values used by the simulation
    pop_size = 1000
    vacc_percentage = 0.1
    initial_infected = 10

    # Make a new instance of the simulation
    sim = Simulation(virus, pop_size, vacc_percentage, initial_infected)

    # Run the simulation
    sim.run()
