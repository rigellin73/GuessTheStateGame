from game_screen import GameScreen
from states_map import StatesMap, NUMBER_OF_STATES
from states_data import StatesData

game_screen = GameScreen()
states_map = StatesMap()
states_data = StatesData()

game_over = False

while not game_over:
    guessed_states = states_map.get_number_of_guessed_states()
    dialog_window_title = f"{guessed_states}/{NUMBER_OF_STATES} States Correct"

    try:
        input_name = game_screen.ask_for_input(dialog_window_title).title()
        state_position = states_data.get_state_position(input_name)
        if state_position:
            states_map.add_state(input_name,state_position)
    except AttributeError:
        game_over = True
        states_map.show_lose_message()

    if guessed_states == NUMBER_OF_STATES:
        game_over = True
        states_map.show_win_message()

states_data.export_not_guessed_states_csv(states_map.guessed_states)

game_screen.screen.exitonclick()
