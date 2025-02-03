from game_screen import GameScreen
from states_map import StatesMap
from states_data import StatesData

NUMBER_OF_STATES = 50

game_screen = GameScreen()
states_map = StatesMap()
states_data = StatesData()
guessed_states = []
game_over = False

while not game_over:
    input_name = game_screen.ask_for_input()

    if input_name:
        state_position = states_data.get_state_position(input_name)
        if state_position:
            states_map.add_state(input_name,state_position)
            if input_name not in guessed_states:
                guessed_states.append(input_name)
    else:
        game_over = True

    if len(guessed_states) == NUMBER_OF_STATES:
        game_over = True
        states_map.show_win_message()

game_screen.screen.exitonclick()
