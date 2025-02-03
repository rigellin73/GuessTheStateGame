import pandas

DATA_FILE = "50_states.csv"

class StatesData:
    def __init__(self):
        self.data = pandas.read_csv(DATA_FILE)

    def find_state(self, name):
        return self.data[self.data.state == name]
