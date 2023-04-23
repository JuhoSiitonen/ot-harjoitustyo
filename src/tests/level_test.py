import unittest
import pygame
from level import Level

level_map = ['00000000000000000000',
             '00000000000000000000',
             '00000000000000000000',
             'xxx000000x0000000000',
             'xxx000000P0G00000xxx',
             '0000000xxxxx00000xxx',
             '0000000xxxxx00000xxx',
             'xxxxx00000000B00E00B',
             'xxxxxxxx000000xxxxxx']

CELL_SIZE = 64

class TestLevel(unittest.TestCase):
    def setUp(self):
        self.level = Level(level_map)

    def test_camera_center(self):
        self.level.camera()
        self.assertEqual(self.level.camera_shift, 0)

    def test_camera_right(self):
        player = self.level.player_cell.sprite
        player.rect.x = 199
        player.direction.x = -1
        self.level.camera()
        self.assertEqual(self.level.camera_shift, 7)

    def test_camera_left(self):
        player = self.level.player_cell.sprite
        player.rect.x = 1001
        player.direction.x = 1
        self.level.camera()
        self.assertEqual(self.level.camera_shift, -7)

    def test_horizontal_collision_left(self):
        player = self.level.player_cell.sprite
        player.rect.x = 100
        player.direction.x = -1
        self.level.horizontal_collision()
        self.assertNotEqual(player.rect.x, 100)
    
    def test_horizontal_collision_right(self):
        player = self.level.player_cell.sprite
        player.rect.x = 1100
        player.direction.x = 1
        self.level.horizontal_collision()
        self.assertNotEqual(player.rect.x, 1100)
    
    def test_vertical_collision_bottom(self):
        player = self.level.player_cell.sprite
        start = player.rect.y
        player.rect.y += 40
        player.direction.y = +1
        self.level.vertical_collision()
        self.assertEqual(player.rect.y, start)

    def test_vertical_collision_top(self):
        player = self.level.player_cell.sprite
        start = player.rect.y
        player.rect.y -= 40
        player.direction.y = -1
        self.level.vertical_collision()
        self.assertEqual(player.rect.y, start)

    def test_level_completed(self):
        player = self.level.player_cell.sprite
        player.rect.x += 100
        self.assertEqual(self.level.level_completion(), True)

    def test_level_not_completed(self):
        player = self.level.player_cell.sprite
        player.rect.x += 20
        self.assertEqual(self.level.level_completion(), False)

    def test_enemy_movement(self):
        for enemy in self.level.enemies:
            start = enemy.rect.x
        self.level.enemy_movement()
        for enemy in self.level.enemies:
            self.assertNotEqual(enemy.rect.x, start)

    def test_player_demise_out_of_bounds(self):
        player = self.level.player_cell.sprite
        player.rect.y = 700
        self.assertEqual(self.level.player_demise(), True)

    def test_player_demise_enemy_collision(self):
        player = self.level.player_cell.sprite
        player.rect.x += 450
        player.rect.y += 200
        self.assertEqual(self.level.player_demise(), True)

    def test_player_demise_no_collision_in_bounds_false(self):
        self.assertEqual(self.level.player_demise(), False)

