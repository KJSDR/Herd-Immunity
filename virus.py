class Virus(object):
    # Properties and attributes of the virus used in Simulation.
    def __init__(self, name, repro_rate, mortality_rate):
        self.name = name
        self.repro_rate = repro_rate
        self.mortality_rate = mortality_rate

def test_valid_virus_attributes():
    virus = Virus("TestVirus", 0.5, 0.25)
    assert virus.repro_rate == 0.5
    assert virus.mortality_rate == 0.25

def test_invalid_virus_attributes():
    try:
        Virus("TestVirus", -0.1, 1.5)
    except ValueError:
        assert True



# Test this class
if __name__ == "__main__":
    virus = Virus("HIV", 0.8, 0.3)
    assert virus.name == "HIV"
    assert virus.repro_rate == 0.8
    assert virus.mortality_rate == 0.3
    print("All tests passed!")