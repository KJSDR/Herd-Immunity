import datetime

class SimulationLogger:
    """Handles logging for the simulation process."""

    def __init__(self, filename):
        """Creates or opens the log file to start recording."""
        self.filename = filename
        with open(self.filename, 'w'): pass  # Ensure the file is created/empty at start

    def log_metadata(self, population_size, vaccinated_percentage, virus_type, mortality_rate, reproduction_rate, initial_infected):
        """Logs basic metadata at the start of the simulation."""
        timestamp = datetime.datetime.now()
        with open(self.filename, 'a') as log_file:
            log_file.write(f"Timestamp: {timestamp}\n")
            log_file.write(f"Population Size: {population_size}\n")
            log_file.write(f"Initial Infected: {initial_infected}\n")
            log_file.write(f"Virus: {virus_type}\n")
            log_file.write(f"Mortality Rate: {mortality_rate}\n")
            log_file.write(f"Reproduction Rate: {reproduction_rate}\n\n")

    def record_interactions(self, step, interaction_count, new_infections):
        """Logs interaction statistics for each simulation step."""
        with open(self.filename, 'a') as log_file:
            log_file.write(f"Step {step}: Interactions = {interaction_count}, New Infections = {new_infections}\n\n")

    def record_survival_stats(self, step, total_population, fatalities, living, dead, vaccinated):
        """Logs survival data at each step."""
        with open(self.filename, 'a') as log_file:
            log_file.write(f"Step {step}: Total Population = {total_population}, Fatalities = {fatalities}\n")
            log_file.write(f"Living: {living}, Dead: {dead}, Vaccinated: {vaccinated}\n\n")

    def log_summary(self, survivors, deaths, total_vaccinated, total_interactions):
        """Logs a final summary of the simulation once it ends."""
        with open(self.filename, 'a') as log_file:
            log_file.write("Final Summary:\n")
            log_file.write(f"Survivors: {survivors}\n")
            log_file.write(f"Deaths: {deaths}\n")
            log_file.write(f"Total Vaccinated: {total_vaccinated}\n")
            log_file.write(f"Total Interactions: {total_interactions}\n")
            log_file.write("Simulation completed.\n\n")
