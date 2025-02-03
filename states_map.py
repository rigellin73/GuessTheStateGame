from turtle import Turtle
from game_screen import SCREEN_HEIGHT, MAP_SHAPE

NUMBER_OF_STATES = 50

ALIGN = "center"
STATE_TEXT_FONT = ("Arial", 12, "normal")
FINAL_MESSAGE_FONT = ("Arial", 20, "bold")
WIN_MESSAGE = "Congratulations! You found all the states!"
FINAL_MESSAGE_HEIGHT = SCREEN_HEIGHT / 2 - 50

class StatesMap:
    def __init__(self):
        self.s_map = Turtle(MAP_SHAPE)
        self.s_name = Turtle()
        self.s_name.hideturtle()
        self.s_name.penup()
        self.guessed_states = []

    def write_text(self, text, position, align, font):
        self.s_name.goto(position)
        self.s_name.write(text, False, align, font)

    def add_state(self, state_name, position):
        self.write_text(state_name, position, ALIGN, STATE_TEXT_FONT)
        if state_name not in self.guessed_states:
            self.guessed_states.append(state_name)

    def show_win_message(self):
        self.write_text(WIN_MESSAGE, (0, FINAL_MESSAGE_HEIGHT), ALIGN, FINAL_MESSAGE_FONT)

    def show_lose_message(self):
        message = f"You found {len(self.guessed_states)} / {NUMBER_OF_STATES} States"
        self.write_text(message, (0, FINAL_MESSAGE_HEIGHT), ALIGN, FINAL_MESSAGE_FONT)

    def get_number_of_guessed_states(self):
        return len(self.guessed_states)
