class Logger(object):
    def __init__(self, file_name):
        # Initialize the logger with the given file name
        # Open the file in write mode to start writing logs.
        self.file_name = file_name
        self.file = open(file_name, 'w')  # Open file in write mode

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num):
        # Log the initial metadata (population size, vaccination percentage, virus name, etc.)
        metadata = f"Population Size: {pop_size}\tVaccination Percentage: {vacc_percentage * 100}%\t" \
                   f"Virus: {virus_name}\tMortality Rate: {mortality_rate * 100}%\tReproduction Rate: {basic_repro_num}\n"
        self.file.write(metadata)

    def log_interactions(self, step_number, number_of_interactions, number_of_new_infections):
        # Log the interactions during each time step
        interaction_log = f"Step: {step_number}\tInteractions: {number_of_interactions}\t" \
                          f"New Infections: {number_of_new_infections}\n"
        self.file.write(interaction_log)

    def log_infection_survival(self, step_number, population_count, number_of_new_fatalities):
        # Log survival and fatalities during each time step
        survival_log = f"Step: {step_number}\tPopulation: {population_count}\t" \
                       f"New Fatalities: {number_of_new_fatalities}\n"
        self.file.write(survival_log)

    def close(self):
        # Close the log file when the simulation is done
        self.file.close()
