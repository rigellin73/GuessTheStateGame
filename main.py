from game_screen import setup_screen
from states_map import StatesMap
from states_data import StatesData

game_screen = setup_screen()
states_map = StatesMap()
states_data = StatesData()

input_name = input("Enter state name: ").title()

state_position = states_data.get_state_position(input_name)
if state_position:
    states_map.add_state(input_name,state_position)
else:
    print("no such state")

game_screen.exitonclick()
