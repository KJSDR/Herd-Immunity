class Logger:
    def __init__(self, file_name):
        '''
        Initialize the logger with a file name.
        '''
        self.file_name = file_name

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate, repro_rate):
        '''
        Log the metadata of the simulation.
        '''
        with open(self.file_name, 'a') as file:
            file.write(f"--- New Simulation ---\n")
            file.write(f"Population Size: {pop_size}\n")
            file.write(f"Vaccination Percentage: {vacc_percentage}\n")
            file.write(f"Virus Name: {virus_name}\n")
            file.write(f"Mortality Rate: {mortality_rate}\n")
            file.write(f"Reproductive Rate: {repro_rate}\n")
            file.write("\n")

    def log_infection_survival(self, time_step, alive, deaths):
        '''
        Log the infection survival data after a time step.
        '''
        with open(self.file_name, 'a') as file:
            file.write(f"Time Step {time_step}:\n")
            file.write(f"  Alive: {alive}\n")
            file.write(f"  Deaths: {deaths}\n")
            file.write("\n")


    def log_final_summary(self, time_steps, pop_size, survivors, deaths, vaccinated):
        '''
        Log the final summary.
        '''
        with open(self.file_name, 'a') as file:
            file.write("--- Final Summary ---\n")
            file.write(f"Time Steps: {time_steps}\n")
            file.write(f"Population Size: {pop_size}\n")
            file.write(f"Survivors: {survivors}\n")
            file.write(f"Deaths: {deaths}\n")
            file.write(f"Vaccinated Survivors: {vaccinated}\n")
            file.write("\n")

    def log_total_infections(self, total_infected):
            '''
            Log the total number of infections
            '''
            with open(self.file_name, 'a') as file:
                file.write(f"--- Total Infections ---\n")
                file.write(f"Total Infected: {total_infected}\n")
                file.write("\n")