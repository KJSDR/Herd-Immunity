import random
from virus import Virus

class Person:
    def __init__(self, _id, vaccinated, infection=None):
        """
        Represents a person in the simulation.
        """
        self._id = _id
        self.vaccinated = vaccinated
        self.infection = infection
        self.is_alive = True
        self.is_dead = False

    def check_for_death(self):
        """
        Checks if the person dies from the infection based on mortality rate.
        """
        if self.infection and not self.vaccinated and random.random() < self.infection.mortality_rate:
            self.is_alive = False
            self.is_dead = True

    def survive_infection(self):
        """
        Determines if the person survives the infection.
        """
        if self.infection:
            survival_chance = random.random()
            if survival_chance < self.infection.mortality_rate:
                self.is_alive = False
                return False
            self.vaccinated = True
            self.infection = None
            return True
        return None

def test_survival():
    test_virus = Virus("TestVirus", 0.5, 0.25)
    person = Person(1, False, test_virus)
    survived = person.survive_infection()
    assert survived in [True, False]

def test_vaccinated_person():
    person = Person(2, True)
    assert person.vaccinated
    assert person.infection is None

if __name__ == "__main__":
    vaccinated = Person(1, True)
    assert vaccinated._id == 1
    assert vaccinated.is_alive
    assert vaccinated.vaccinated
    assert vaccinated.infection is None

    unvaccinated = Person(2, False)
    assert unvaccinated._id == 2
    assert unvaccinated.is_alive
    assert not unvaccinated.vaccinated
    assert unvaccinated.infection is None

    virus = Virus("Dysentery", 0.7, 0.2)
    infected_person = Person(3, False, virus)
    assert infected_person._id == 3
    assert infected_person.is_alive
    assert not infected_person.vaccinated
    assert infected_person.infection == virus

    people = [Person(i, False, virus) for i in range(1, 101)]
    survivors, non_survivors = 0, 0
    for person in people:
        if person.survive_infection():
            survivors += 1
        else:
            non_survivors += 1

    print(f"Survived: {survivors}")
    print(f"Did not survive: {non_survivors}")
    print(f"Expected Mortality Rate: {virus.mortality_rate}")
    print(f"Observed Mortality Rate: {non_survivors / len(people):.2f}")

    uninfected_people = [Person(i, False) for i in range(101, 201)]
    infected_count = 0
    for person in uninfected_people:
        if random.random() < virus.repro_rate:
            person.infection = virus
            infected_count += 1

    print(f"Infected: {infected_count}")
    print(f"Uninfected: {len(uninfected_people) - infected_count}")
    print(f"Expected Infection Rate: {virus.repro_rate}")
    print(f"Observed Infection Rate: {infected_count / len(uninfected_people):.2f}")
