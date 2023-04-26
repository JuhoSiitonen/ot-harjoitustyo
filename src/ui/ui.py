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
    def __init__(self):
        self.create_window()
        self.time_attack = False

    def create_window(self):
        sg.set_options(font = "Franklin 20")
        self.layout = [
            [sg.Text("Select level")],
            [sg.Button("Level 1"), sg.Button("Level 2")],
            [sg.Button("Time Attack"), sg.Button("Exit")]
            ]
        self.window = sg.Window("Jumpman", self.layout)

    def check_time_attack(self):
        if not self.time_attack:
            self.time_attack = True
            self.window["Time Attack"].update(button_color = ("blue"))
        else:
            self.time_attack = False
            self.window["Time Attack"].update(button_color = None)

    def run(self):
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
        display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

        clock = Clock()
        level = Level(level_map)
        renderer = Renderer(display, level, self.time_attack)
        event_handling = EventHandling()
        game = Game(level, clock, event_handling, renderer)

        pygame.display.set_caption("Jumpman")
        pygame.init()

        game.start()
