import pandas

DATA_FILE = "50_states.csv"

class StatesData:
    def __init__(self):
        self.data = pandas.read_csv(DATA_FILE)

    def get_state_position(self, name):
        pos = ()
        if name:
            state_info = self.data[self.data.state == str(name)]
            try:
                pos = (state_info.x.item(), state_info.y.item())
            except ValueError:
                pass

        return pos
