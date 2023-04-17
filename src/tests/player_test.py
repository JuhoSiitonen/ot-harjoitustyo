import unittest
import pygame
from player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player((50, 50))

    def check_sprite_coordinates_equal(self, sprite, x, y):
        self.assertEqual(sprite.rect.x, x)
        self.assertEqual(sprite.rect.y, y)

    def test_player_can_move(self):
        self.check_sprite_coordinates_equal(self.player, 50, 50)
        self.player.movement(dx=50, dy=50)
        self.check_sprite_coordinates_equal(self.player, 100, 100)

    def test_player_can_jump(self):
        self.player.jump()
        self.assertEqual(self.player.direction.y, -15)

    def test_player_move_method_works_right(self):
        self.player.direction.x = 1
        self.player.move()
        self.check_sprite_coordinates_equal(self.player, 57, 50)

    def test_player_move_method_works_left(self):
        self.player.direction.x = -1
        self.player.move()
        self.check_sprite_coordinates_equal(self.player, 43, 50)

    def test_gravity_alone_on_direction(self):
        self.player.apply_gravity()
        self.assertEqual(self.player.direction.y, 0.7)

    def test_gravity_on_movement(self):
        self.player.apply_gravity()
        self.player.apply_gravity()
        self.check_sprite_coordinates_equal(self.player, 50, 51)

    def test_jump(self):
        self.player.jump()
        self.assertEqual(self.player.direction.y, -15)

    
