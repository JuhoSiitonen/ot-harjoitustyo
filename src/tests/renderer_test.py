import time
import unittest
import pygame
from support.renderer import Renderer
from logic.level import Level

level_map = ['00000000000000000000',
             '00000000000000000000',
             '00000000000000000000',
             'xxx000000x0000000000',
             'xxx0000ACP0G00000xxx',
             '0000000xxxxx00000xxx',
             '0000000xxxxx00000xxx',
             'xxxxx0000000000BE00B',
             'xxxxxxxx000000xxxxxx']

CELL_SIZE = 64
DISPLAY_HEIGHT = CELL_SIZE * len(level_map)
DISPLAY_WIDTH = 1200
"""
class TestRenderer(unittest.TestCase):
    def setUp(self):
        display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
        self.level = Level(level_map)
        time_attack = True
        self.clock = pygame.time.Clock()
        self.renderer = Renderer(display, self.level, time_attack)

    def test_time_counter_timeout(self):
        self.renderer.time_counter()
        self.assertEqual(self.timeout, False)
        self.clock.tick(0)
"""