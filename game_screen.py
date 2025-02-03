from turtle import Screen
from states_map import MAP_SHAPE

SCREEN_WIDTH = 750
SCREEN_HEIGHT = 500
SCREEN_TITLE = "U.S. States Game"
DIALOG_WINDOW_PROMPT = "What's another state's name?"

class GameScreen():
    def __init__(self):
        self.screen = Screen()
        self.setup_screen()

    def setup_screen(self):
        self.screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.screen.addshape(MAP_SHAPE)
        self.screen.title(SCREEN_TITLE)

    def ask_for_input(self, dialog_window_title):
        try:
            return self.screen.textinput(dialog_window_title, DIALOG_WINDOW_PROMPT)
        except AttributeError:
            return ""
