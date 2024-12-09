import random
from virus import Virus

class Person(object):
    # Define a person.
    def __init__(self, _id, is_vaccinated, infection=None):
        # A person has an id, is_vaccinated, and possibly an infection
        self._id = _id  # int
        self.is_vaccinated = is_vaccinated  # Boolean value for vaccination status
        self.infection = infection  # This will hold a Virus object or None
        self.is_alive = True  # By default, the person is alive

    def did_survive_infection(self):
        # This method checks if a person survived an infection. 
        if self.infection:
            # Generate a random number between 0.0 and 1.0
            survival_chance = random.random()  # Random number between 0.0 and 1.0
            # Check if the random number is less than the mortality rate of the virus
            if survival_chance < self.infection.mortality_rate:
                # Person dies, mark as not alive
                self.is_alive = False
                return False  # Person did not survive
            else:
                # Person survives, they become vaccinated
                self.is_vaccinated = True
                return True  # Person survived
        return True  # If no infection, the person is considered to have survived

if __name__ == "__main__":
    # Test a vaccinated person
    vaccinated_person = Person(1, True)
    assert vaccinated_person._id == 1
    assert vaccinated_person.is_alive is True
    assert vaccinated_person.is_vaccinated is True
    assert vaccinated_person.infection is None

    # Create an unvaccinated person and test their attributes
    unvaccinated_person = Person(2, False)
    assert unvaccinated_person._id == 2
    assert unvaccinated_person.is_alive is True
    assert unvaccinated_person.is_vaccinated is False
    assert unvaccinated_person.infection is None

    # Test an infected person. An infected person has an infection/virus
    virus = Virus("Dysentery", 0.7, 0.2)  # Virus with 70% mortality rate and 20% infection rate
    infected_person = Person(3, False, virus)
    assert infected_person._id == 3
    assert infected_person.is_vaccinated is False
    assert infected_person.infection is virus

    # Test survival of an infected person
    survived = infected_person.did_survive_infection()
    if survived:
        assert infected_person.is_vaccinated is True
        assert infected_person.is_alive is True
    else:
        assert infected_person.is_alive is False

    # Create 100 people and resolve survival of infection based on mortality rate
    people = []
    for i in range(1, 101):
        person = Person(i, random.random() < 0.5)  # 50% chance of vaccination
        if random.random() < 0.5:  # 50% chance of being infected
            person.infection = virus
        people.append(person)

    # Track survival rates
    did_survive = 0
    did_not_survive = 0

    for person in people:
        survived = person.did_survive_infection()
        if person.is_alive:
            did_survive += 1
        else:
            did_not_survive += 1

    print(f"Survived: {did_survive} people")
    print(f"Did not survive: {did_not_survive} people")
