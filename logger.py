class Logger:
    def __init__(self, file_name):
        """
        Initializes the logger with the specified file name.
        """
        self.file_name = file_name

    def write_metadata(self, population_size, vaccination_rate, virus_name, death_rate, reproduction_rate):
        """
        Logs the simulation metadata.
        """
        with open(self.file_name, 'a') as file:
            file.write(f"--- New Simulation ---\n")
            file.write(f"Population Size: {population_size}\n")
            file.write(f"Vaccination Rate: {vaccination_rate}\n")
            file.write(f"Virus: {virus_name}\n")
            file.write(f"Mortality Rate: {death_rate}\n")
            file.write(f"Reproductive Rate: {reproduction_rate}\n")
            file.write("\n")

    def log_infection_status(self, timestep, alive_count, death_count):
        """
        Logs the infection survival stats at each timestep.
        """
        with open(self.file_name, 'a') as file:
            file.write(f"Time Step {timestep}:\n")
            file.write(f"  Alive: {alive_count}\n")
            file.write(f"  Deaths: {death_count}\n")
            file.write("\n")

    def log_summary(self, total_steps, population_size, survivors, fatalities, vaccinated_survivors):
        """
        Logs the final summary at the end of the simulation.
        """
        with open(self.file_name, 'a') as file:
            file.write("--- Final Summary ---\n")
            file.write(f"Time Steps: {total_steps}\n")
            file.write(f"Population Size: {population_size}\n")
            file.write(f"Survivors: {survivors}\n")
            file.write(f"Fatalities: {fatalities}\n")
            file.write(f"Vaccinated Survivors: {vaccinated_survivors}\n")
            file.write("\n")

    def log_total_infected(self, total_infected):
        """
        Logs the total infections recorded.
        """
        with open(self.file_name, 'a') as file:
            file.write(f"--- Total Infections ---\n")
            file.write(f"Total Infected: {total_infected}\n")
            file.write("\n")
