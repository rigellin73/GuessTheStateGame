from turtle import Turtle

MAP_SHAPE = "blank_states_img.gif"
ALIGN = "center"
FONT = ("Arial", 12, "normal")

class StatesMap:
    def __init__(self):
        self.s_map = Turtle(MAP_SHAPE)
        self.s_name = Turtle()
        self.s_name.hideturtle()
        self.s_name.penup()

    def add_state(self, state_name, x, y):
        self.s_name.goto(x, y)
        self.s_name.write(state_name, False, ALIGN, FONT)
