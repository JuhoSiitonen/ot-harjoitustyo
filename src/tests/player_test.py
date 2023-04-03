import unittest
import pygame
import player import Player


class TestPlayer(unittest.TestCase):
    def setup(self):
        self.player = Player((50,50))

    def check_sprite_coordinates_equal(self, sprite, x, y):
        self.assertEqual(sprite.rect.x, x)
        self.assertEqual(sprite.rect.y, y)

    def test_player_can_move(self):
        self.check_sprite_coordinates_equal(self.player, 50, 50)
        self.player.movement(dx=50, dy=50)
        self.check_sprite_coordinates_equal(self.player, 100, 100)
    