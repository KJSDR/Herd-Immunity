class Virus(object):
    # Properties and attributes of the virus used in Simulation.
    def __init__(self, name, repro_rate, mortality_rate):
        # Define the attributes of your virus
        self.name = name  # Name of the virus (e.g., "HIV", "Sniffles")
        self.repro_rate = repro_rate  # Reproduction rate (basic reproduction number)
        self.mortality_rate = mortality_rate  # Mortality rate of the virus

# Test this class
if __name__ == "__main__":
    # Test your virus class by making an instance and confirming 
    # it has the attributes you defined
    virus = Virus("HIV", 0.8, 0.3)
    assert virus.name == "HIV"
    assert virus.repro_rate == 0.8
    assert virus.mortality_rate == 0.3

    print("Virus test passed!")
