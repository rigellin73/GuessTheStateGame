import turtle

from game_screen import GameScreen
from states_map import StatesMap
from states_data import StatesData

game_screen = GameScreen()
states_map = StatesMap()
states_data = StatesData()
game_over = False

while not game_over:
    input_name = game_screen.ask_for_input()

    if input_name:
        state_position = states_data.get_state_position(input_name)
        if state_position:
            states_map.add_state(input_name,state_position)
        else:
            print("no such state")
    else:
        game_over = True

game_screen.screen.exitonclick()
