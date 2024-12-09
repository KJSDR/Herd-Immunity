import random
from virus import Virus

class Individual:
    """Represents an individual in the population."""

    def __init__(self, id, vaccinated, infection=None):
        """Initializes an individual with ID, vaccination status, and optional infection."""
        self.id = id
        self.vaccinated = vaccinated
        self.infection = infection
        self.alive = True

    def survive_or_die(self):
        """Determines if the person survives the infection based on the mortality rate."""
        if self.infection:
            survival_prob = random.random()
            print(f"Person {self.id} | Infection: {self.infection.name} | Survival Chance: {survival_prob}, Mortality: {self.infection.mortality_rate}")
            if survival_prob < self.infection.mortality_rate:
                self.alive = False
                self.infection = None
                print(f"Person {self.id} succumbed to the infection.")
                return False
            else:
                self.vaccinated = True
                self.infection = None
                print(f"Person {self.id} survived and is now vaccinated.")
                return True
        return True

if __name__ == "__main__":
    # Example test cases for individuals
    virus_instance = Virus("TestVirus", 0.5, 0.2)

    # Create an unvaccinated person
    person1 = Individual(1, False, virus_instance)
    person2 = Individual(2, True)

    # Simulate survival
    result1 = person1.survive_or_die()
    result2 = person2.survive_or_die()
    
    print(f"Person 1 survived: {result1}")
    print(f"Person 2 survived: {result2}")
