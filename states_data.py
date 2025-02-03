import pandas

DATA_FILE = "50_states.csv"
EXPORT_DATA_FILE = "states_to_learn.csv"

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

    def export_not_guessed_states_csv(self, guessed_states):
        not_guessed_states = []
        for state in self.data.state:
            if not state in guessed_states:
                not_guessed_states.append(state)
        export_data = pandas.DataFrame(not_guessed_states)
        export_data.to_csv(EXPORT_DATA_FILE)
