import threading
import sys
import PySimpleGUI as sg
import pygame
from database_connection import get_db_connection
from logic.level import Level
from logic.game import Game
from support.renderer import Renderer
from support.event_handling import EventHandling
from support.clock import Clock
from support.helper_functions import level_file_reader
from repositories.highscore_repository import HighscoreRepository
from settings import CELL_SIZE, DISPLAY_WIDTH

class UI:
    """Class to initialize a PySimpleGUI Ui window and subsequently open
        the Pygame game loop.

        Attributes:
            time_attack: Tells if user selected the time attack mode by clicking 
                the time attack button. 
            layout: PySimpleGUI window layout, font and size
            level_map: Nested list with level data, used to determine how many levels
                are in the game, and thus have the buttons for opening them.
            highscores: List of tuples, highscores in order of level and by completion time.
            window: Instance of the PySimpleGUI window.
            window2: Instance of PySimpleGUI window for showcasing highscores.
            window2_active = Bool value, if true run loop will run code to display
                highscore window.
            DB = Database connection object.
            highscore_repository: Object to handle database operations regarding highscores.
    """

    def __init__(self):
        """Class constructor to create a PySimpleGUi UI window by first 
        reading from data folders levels text file and using that 
        information to create buttons for the levels to the window. Also
        initializes a database repository object to interact with highscore 
        database.
        """

        self.check_levels_file()
        self.DB = get_db_connection()
        self.highscore_repository = HighscoreRepository(self.DB)
        self.create_window()
        self.time_attack = False
        self.window2_active = False

    def check_levels_file(self):
        """Calls support function to read levels.txt file and set the return 
        statement which is a list of levels in level_maps variable.
        """

        self.level_maps = level_file_reader()

    def check_highscores_file(self):
        """Method to call database repository method for reading highscore
        table from database. Database repository returns a list of tuples 
        which are set to attribute self.highscores.
        """

        self.highscores = self.highscore_repository.highscores_list()

    def create_window(self):
        """Creates the PySimpleGUI window with a layout of buttons with a selected color 
        and a selected font and font size. Level buttons are created as a list 
        comprehension and concatenated to the window layout.
        """

        sg.set_options(font = "Franklin 20")
        lvls = len(self.level_maps)
        header = [[sg.Text("Select level")]]
        lvl_buttons = [[sg.Button(f"Level {i}") for i in range(1, lvls+1)]]
        end_buttons = [
            [sg.Button("Time Attack", button_color = (None, "grey")),
            sg.Button("Highscores"),
            sg.Button("Exit")]]
        layout = header + lvl_buttons + end_buttons
        self.window = sg.Window("Jumpman", layout)

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

    def create_highscore_window(self):
        """Creates a PysimpleGUI window for showing 3 highscores per
        level, the highscores come from a sqlite database as a list of tuples
        and for loop is used to make rows to PySimpleGUI window. Variables header,
        scores and end_buttons used to concatenate one single layout for PySimpleGUi 
        window.
        """

        self.check_highscores_file()
        header = [[sg.Text("Best times per level")]]
        scores = []
        if self.highscores:
            for line in self.highscores:
                scores += [[sg.Text(f"Level {line[0]} time: {line[1]}")]]
        end_buttons = [[sg.Button("Erase scores"), sg.Button("Exit")]]
        layout = header + scores + end_buttons
        self.window2 = sg.Window("Jumpman Highscores", layout)

    def run_highscore_window(self):
        """Method to check PySimpleGUI events on the highscore window, all events 
        end up closing the window, but erase scores will also delete rows from database.
        """

        event2, __ = self.window2.read() # pylint: disable=unused-variable
        if event2 in (sg.WIN_CLOSED, "Exit", "Erase scores"):
            self.window2_active = False
            if event2 == "Erase scores":
                self.highscore_repository.erase_highscores()
            self.window2.close()

    def main_menu_window_events(self, event):
        """Method to handle main menu button events. Time attack changes the time
        attack bool value to True, buttons for the levels found in levels.txt file
        are checked with a for loop and they begin a new Thread to handle a Pygame 
        window. This is necessary to handle closing Pygame in a way that PySimpleGUI 
        won't shutdown. Highscore button changes window2 to be active and the Run method
        loop will call the run_highscore_window method (after the create highscore window
        function call).

        Args:
            event (str): Str which is the key value of the buttons on the PySimpleGUI
            window. 
        """

        if event in (sg.WIN_CLOSED, "Exit"):
            sys.exit()
        if event == "Time Attack":
            self.check_time_attack()
        for i in range (1, len(self.level_maps)+1):
            if event == f"Level {i}":
                pygame_thread = threading.Thread(target=self.run_game(self.level_maps[i-1], i))
                pygame_thread.start()
        if event == "Highscores" and not self.window2_active:
            self.window2_active = True
            self.create_highscore_window()

    def run(self):
        """Method to run a loop to read window events such as mouse clicks on the 
        buttons. According to the button events either main menu window events 
        method is checked or if the highscore button is pressed a new PySimpleGUI
        window is opened and run highscore window method will check its events.
        """

        while True:
            event, _ = self.window.read() # pylint: disable=unused-variable
            self.main_menu_window_events(event)
            if self.window2_active:
                self.run_highscore_window()


    def run_game(self, level_map, level_number):
        """Method initializes the depencies which need to be injected to instantiate
        a game class object and then sets Pygame window caption and initializes a 
        Pygame window. 

        Args:
            level_map (list): Nested list with the level layout.
            level_number (int): Integer to tell which level is played.
        """
        DISPLAY_HEIGHT = len(self.level_maps[level_number-1]) * CELL_SIZE
        display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

        clock = Clock()
        level = Level(level_map, level_number)
        renderer = Renderer(display, level, self.time_attack)
        event_handling = EventHandling()
        game = Game(level, clock, event_handling, renderer, self.time_attack, self.highscore_repository)

        pygame.display.set_caption("Jumpman")
        pygame.init()

        game.start()
