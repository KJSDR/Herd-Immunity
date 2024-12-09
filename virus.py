class Virus(object):
    """Represents a virus with properties and attributes used in the simulation."""
    
    def __init__(self, name, repro_rate, mortality_rate):
        self.name = name
        self.repro_rate = repro_rate
        self.mortality_rate = mortality_rate

    def __str__(self):
        """Provides a string representation of the virus for easier logging and debugging."""
        return f"{self.name} (Reproduction Rate: {self.repro_rate}, Mortality Rate: {self.mortality_rate})"

# Example Usage
if __name__ == "__main__":
    # Create virus instances
    ebola_virus = Virus("Ebola", 1.9, 0.6)
    chickenpox_virus = Virus("Chickenpox", 0.8, 0.1)
    hiv_virus = Virus("HIV", 0.8, 0.3)

    # Test virus attributes
    assert hiv_virus.name == "HIV"
    assert hiv_virus.repro_rate == 0.8
    assert hiv_virus.mortality_rate == 0.3

    assert chickenpox_virus.name == "Chickenpox"
    assert chickenpox_virus.repro_rate == 0.8
    assert chickenpox_virus.mortality_rate == 0.1

    assert ebola_virus.name == "Ebola"
    assert ebola_virus.repro_rate == 1.9
    assert ebola_virus.mortality_rate == 0.6

    # Print virus details
    print(ebola_virus)
    print(chickenpox_virus)
    print(hiv_virus)
