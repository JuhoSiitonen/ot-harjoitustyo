import threading
import PySimpleGUI as sg
import pygame
from level import Level
from game import Game
from renderer import Renderer
from event_handling import EventHandling
from clock import Clock
from settings import *

class UI:
    def __init__(self):
        self.create_window()
        self.max_level = 1

    def create_window(self):
        sg.set_options(font = "Franklin 20")
        self.layout = [
            [sg.Text("Select level")],
            [sg.Button("Level 1"), sg.Button("Level 2")],
            [sg.Button("Exit")]
            ]
        self.window = sg.Window("Jumpman", self.layout)

    def run(self):
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED:
                break
            if event == "Level 1":
                pygame_thread = threading.Thread(target=self.run_game(level_map_1))
                pygame_thread.start()
        pygame_thread.join()

    def run_game(self, level_map):
        display = pygame.display.set_mode((display_width, display_height))

        clock = Clock()
        level = Level(level_map)
        renderer = Renderer(display, level)
        event_handling = EventHandling()
        game = Game(level, clock, event_handling, renderer)

        pygame.display.set_caption("Jumpman")
        pygame.init()

        game.start()
