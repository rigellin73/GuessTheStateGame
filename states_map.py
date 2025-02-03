from turtle import Turtle

MAP_SHAPE = "blank_states_img.gif"
ALIGN = "center"
STATE_TEXT_FONT = ("Arial", 12, "normal")
WIN_TEXT_FONT = ("Arial", 20, "normal")
WIN_MESSAGE = "Congratulations! You found all the states!"

class StatesMap:
    def __init__(self):
        self.s_map = Turtle(MAP_SHAPE)
        self.s_name = Turtle()
        self.s_name.hideturtle()
        self.s_name.penup()

    def write_text(self, text, position, align, font):
        self.s_name.goto(position)
        self.s_name.write(text, False, align, font)

    def add_state(self, state_name, position):
        self.write_text(state_name, position, ALIGN, STATE_TEXT_FONT)

    def show_win_message(self):
        self.s_name.clear()
        self.write_text(WIN_MESSAGE, (0, 0), ALIGN, WIN_TEXT_FONT)
