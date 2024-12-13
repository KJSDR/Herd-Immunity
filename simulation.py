import random, sys
# random.seed(42)
from person import Person
from logger import Logger
from virus import Virus


class Simulation(object):
    def __init__(self, virus, pop_size, vacc_percentage, initial_infected=1,):
        '''
        Initialize the simulation 
        '''
        print("Initializing simulation...")
        self.logger = Logger("simulation_log.txt")
        self.virus = virus
        self.pop_size = pop_size
        self.vacc_percentage = vacc_percentage
        self.initial_infected = initial_infected
        self.infected_count = initial_infected
        self.population = self._create_population()
        self.newly_infected = []
        

        print(f"Simulation Initialized. Infected count: {self.infected_count}")

        self.logger.write_metadata(
            pop_size, vacc_percentage, virus.name, virus.mortality_rate, virus.repro_rate
        )

    def _create_population(self):
        '''
        creates the initial pop
        '''
        population = []
        for i in range(self.pop_size):
            if i < self.initial_infected:
                population.append(Person(i, is_vaccinated=False, infection=self.virus))
                self.infected_count += 1
            else:
                is_vaccinated = random.random() < self.vacc_percentage
                population.append(Person(i, is_vaccinated=is_vaccinated))
        return population

    def _simulation_should_continue(self):
        '''
        Determines if the simulation should continue.
        '''
        alive_people = [person for person in self.population if person.is_alive]
        if not alive_people or all(person.is_vaccinated for person in alive_people):
            return False
        return True

    def time_step(self):
        '''
        simulates a single time step, including interactions and infection updates
        '''
        for person in self.population:
            if person.is_alive and person.infection:
                interactions = 0
                while interactions < 100:
                    random_person = random.choice(self.population)
                    if random_person.is_alive and random_person != person:
                        self.interaction(person, random_person)
                        interactions += 1

                person.check_for_death()

        self._infect_newly_infected()

    def run(self):
        '''
        Runs Simulation
        '''
        print("Starting Simulation...")
        time_step_counter = 0
        while self._simulation_should_continue():
            time_step_counter += 1
            self.time_step()

            # log final results
            alive = len([p for p in self.population if p.is_alive])
            dead = self.pop_size - alive
            self.logger.log_infection_survival(time_step_counter, alive, dead)

        survivors = len([p for p in self.population if p.is_alive])
        vaccinated = sum([1 for p in self.population if p.is_alive and p.is_vaccinated])
        deaths = self.pop_size - survivors
        self.logger.log_final_summary(time_step_counter, self.pop_size, survivors, deaths, vaccinated)

        self.logger.log_total_infections(self.infected_count)

        clear_log = input("Would you like to clear the log file after this simulation? (y/n): ")
        if clear_log.lower() == 'y':
            with open(self.logger.file_name, 'w') as file:
                file.write("")  # Clear contents
            print(f"Log file '{self.logger.file_name}' has been cleared.")
        else:
            print("Log file was not cleared.")


    def interaction(self, infected_person, random_person):
        '''
        handles an interaction between an infected person and another person
        '''
        if random_person.is_vaccinated or random_person.infection:
            return
        
        if random.random() < self.virus.repro_rate:
            self.newly_infected.append(random_person)
            self.infected_count += 1

        if random_person not in self.newly_infected:
            self.newly_infected.append(random_person)


    def _infect_newly_infected(self):
        '''
        infects all people in the 'newly_infected' list
        '''
        for person in self.newly_infected:
            person.infection = self.virus
        self.newly_infected = []


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 7:
        print("Usage: python3 simulation.py <population_size> <vaccination_percentage> <virus_name> <repro_rate> <mortality_rate> <initial_infected>")
        sys.exit(1)

    # Parse command-line arguments
    pop_size = int(sys.argv[1])
    vacc_percentage = float(sys.argv[2])
    virus_name = sys.argv[3]
    repro_num = float(sys.argv[4])
    mortality_rate = float(sys.argv[5])
    initial_infected = int(sys.argv[6])

    # Create the Virus object
    virus = Virus(virus_name, repro_num, mortality_rate)

    # Initializethe Simulation
    sim = Simulation(virus, pop_size, vacc_percentage, initial_infected)
    sim.run()
