import random
from virus import Virus


class Person(object):
    # Define a person. 
    def __init__(self, _id, is_vaccinated, infection = None):
        self._id = _id  # int
        self.is_vaccinated = is_vaccinated
        self.infection = infection
        self.is_alive = True
        self.has_dead = False

    def check_for_death(self):
        if self.infection and not self.is_vaccinated and random.random() < self.infection.mortality_rate:
            self.is_alive = False
            self.has_dead = True

    def did_survive_infection(self):
        if self.infection:
            survival_chance = random.random()
            if survival_chance < self.infection.mortality_rate:
                #person did not survive
                self.is_alive = False
                return False
            else:
                # person survived
                self.is_vaccinated = True
                self.infection = None
                return True
        return None
    
def test_survive_infection():
    virus = Virus("TestVirus", 0.5, 0.25)
    person = Person(1, False, virus)
    survived = person.did_survive_infection()
    assert survived in [True, False]

def test_vaccinated_person():
    person = Person(2, True)
    assert person.is_vaccinated
    assert person.infection is None


if __name__ == "__main__":
    # TODO Define a vaccinated person and check their attributes
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

    # Test an infected person. 
    virus = Virus("Dysentery", 0.7, 0.2)
    infected_person = Person(3, False, virus)
    assert infected_person._id == 3
    assert infected_person.is_alive is True
    assert infected_person.is_vaccinated is False
    assert infected_person.infection == virus

    
    people = [Person(1, False, virus) for i in range(1, 101)]
    did_survive = 0
    did_not_survive = 0

    for person in people:
        if person.did_survive_infection():
            did_survive += 1
        else:
            did_not_survive += 1

    print(f"Survived: {did_survive}")
    print(f"Did not survive: {did_not_survive}")
    print(f"Mortality rate (expected): {virus.mortality_rate}")
    print(f"Mortality rate (observed): {did_not_survive / len(people):.2f}")


    # Stretch challenge
    uninfected_people = [Person(i, False) for i in range(101, 201)]
    infected_count = 0

    for person in uninfected_people:
        if random.random() < virus.repro_rate:
            person.infection = virus 
            infected_count += 1

    print(f"Infected: {infected_count}")
    print(f"Uninfected: {len(uninfected_people) - infected_count}")
    print(f"Infection rate (expected): {virus.repro_rate}")
    print(f"Infection rate (observed): {infected_count / len(uninfected_people):.2f}")