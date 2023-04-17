import unittest
import pygame
from level import Level
from game import Game

class StubClock:
    def tick(self, fps):
        pass

class StubKey_press:
    def __init__(self, key):
        self.key = key
    
    def get(self):
        pressed = {}
        pressed[self.key] = True
        return pressed

class StubEvent_handling:
    def __init__(self, events):
        self.events = events

    def get(self):
        return self.events
    
class StubRenderer:
    def render(self):
        pass

level_map = ['00000000000000000000',
             '00000000000000000000',
             '00000000000000000000',
             'xxx000000x0000000000',
             'xxx000000P0000000xxx',
             '0000000xxxxx00000xxx',
             '0000000xxxxx00000xxx',
             'xxxxx000000000000000',
             'xxxxxxxx000000xxxxxx']

class TestGameLoop(unittest.TestCase):
    def setUp(self):
        self.level = Level(level_map)

    """
    def test_game(self):
        pressed = StubKey_press("pygame.K_RIGHT").get()
        game = Game(
            self.level,
            StubClock(),
            StubEvent_handling(pressed),
            StubRenderer()
        )
        game.start()
    """


