class Virus:
    def __init__(self, name, reproduction_rate, mortality_rate):
        """
        Initializes a virus with specified attributes.
        """
        self.name = name
        self.reproduction_rate = reproduction_rate
        self.mortality_rate = mortality_rate

def test_virus_attributes():
    test_virus = Virus("TestVirus", 0.5, 0.25)
    assert test_virus.reproduction_rate == 0.5
    assert test_virus.mortality_rate == 0.25

def test_invalid_virus():
    try:
        Virus("TestVirus", -0.1, 1.5)
    except ValueError:
        assert True

if __name__ == "__main__":
    virus = Virus("HIV", 0.8, 0.3)
    assert virus.name == "HIV"
    assert virus.reproduction_rate == 0.8
    assert virus.mortality_rate == 0.3
    print("All tests passed!")
