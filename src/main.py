import pygame
import sys
from level import Level
from game import Game
from renderer import Renderer
from event_handling import Event_handling
from clock import Clock


level_map = ['00000000000000000000',
             '00000000000000000000',
             '00000000000000000000',
             'xxx00000000000000000',
             'xxx000000P0000000xxx',
             '0000000xxxxx00000xxx',
             '0000000xxxxx00000xxx',
             'xxxxx000000000000000',
             'xxxxxxxx000000xxxxxx']

CELL_SIZE = 64


def main():
    display_height = CELL_SIZE * len(level_map)
    display_width = 1200
    display = pygame.display.set_mode((display_width, display_height))
    
    clock = Clock()
    level = Level(level_map)
    renderer = Renderer(display, level)
    event_handling = Event_handling()
    game = Game(level, clock, event_handling, renderer)

    pygame.display.set_caption("Jumpman")
    pygame.init()

    game.start()

if __name__ == "__main__":
    main()
