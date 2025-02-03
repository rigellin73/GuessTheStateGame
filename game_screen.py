from turtle import Screen
from map import MAP_SHAPE

SCREEN_WIDTH = 750
SCREEN_HEIGHT = 500
SCREEN_TITLE = "U.S. States Game"

def setup_screen():
    screen = Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.addshape(MAP_SHAPE)
    screen.title(SCREEN_TITLE)
    return screen
