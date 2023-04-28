import threading
import sys
import PySimpleGUI as sg
import pygame
from logic.level import Level
from logic.game import Game
from support.renderer import Renderer
from support.event_handling import EventHandling
from support.clock import Clock
from settings import level_map_1, level_map_2, DISPLAY_HEIGHT, DISPLAY_WIDTH

class UI:
    """Class to initialize a PySimpleGUI Ui window and subsequently open
        the Pygame game loop.

        Attributes:
            time_attack: Tells if user selected the time attack mode by clicking 
            the time attack button. 
            layout: PySimpleGUI window layout, font and size
            window: Instance of the PySimpleGUI window.
    """

    def __init__(self):
        """Class constructor to create a PySimpleGUi UI window. 
        """

        self.create_window()
        self.time_attack = False

    def create_window(self):
        """Creates the PySimpleGUI window with a layout of buttons with a selected color 
        and a selected font and font size.
        """

        sg.set_options(font = "Franklin 20")
        self.layout = [
            [sg.Text("Select level")],
            [sg.Button("Level 1"), sg.Button("Level 2")],
            [sg.Button("Time Attack", button_color = (None, "grey")), sg.Button("Exit")]
            ]
        self.window = sg.Window("Jumpman", self.layout)

    def check_time_attack(self):
        """Checks if Time Attack button has been pressed, if so changes the boolean 
        value for time attack to True and changes the buttons color. Subsequent presses
        change the color and value back.
        """

        if not self.time_attack:
            self.time_attack = True
            self.window["Time Attack"].update(button_color = ("blue"))
        else:
            self.time_attack = False
            self.window["Time Attack"].update(button_color = (None, "grey"))

    def run(self):
        """Method to run a loop to read window events such as mouse clicks on the 
        buttons. According to the button events method either exits the program, 
        starts Pygame with a certain level using a new thread to run it or enables 
        the time attack mode. 
        """

        while True:
            event, values = self.window.read() # pylint: disable=unused-variable
            if event in (sg.WIN_CLOSED, "Exit"):
                sys.exit()
            if event == "Time Attack":
                self.check_time_attack()
            if event == "Level 1":
                pygame_thread = threading.Thread(target=self.run_game(level_map_1))
                pygame_thread.start()
            if event == "Level 2":
                pygame_thread = threading.Thread(target=self.run_game(level_map_2))
                pygame_thread.start()
        pygame_thread.join()

    def run_game(self, level_map):
        """Method initializes the depencies which need to be injected to instantiate
        a game class object and then sets Pygame window caption and initializes a 
        Pygame window. 

        Args:
            level_map (list): Nested list with the level layout.
        """

        display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

        clock = Clock()
        level = Level(level_map)
        renderer = Renderer(display, level, self.time_attack)
        event_handling = EventHandling()
        game = Game(level, clock, event_handling, renderer)

        pygame.display.set_caption("Jumpman")
        pygame.init()

        game.start()
