import turtle
from turtle import Turtle

MAP_SHAPE = "blank_states_img.gif"

class StatesMap(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(MAP_SHAPE)
