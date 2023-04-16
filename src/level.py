import pygame
from cells import Cell
from player import Player


class Level:
    def __init__(self, level_map):
        self.setup(level_map)
        self.camera_shift = 0

    def setup(self, level_map):
        self.cells = pygame.sprite.Group()
        self.player_cell = pygame.sprite.GroupSingle()
        self.all_sprites = pygame.sprite.Group()
        for row_index, row in enumerate(level_map):
            for col_index, col in enumerate(row):
                x = col_index * 64
                y = row_index * 64
                if col == "x":
                    self.cell = Cell((x, y), 64)
                    self.cells.add(self.cell)
                if col == "P":
                    self.player = Player((x, y))
                    self.player_cell.add(self.player)
        self.all_sprites.add(
            self.cells,
            self.player_cell
        )

    def camera(self):
        x = self.player.get_player_x()
        direction = self.player.get_direction()
        if x < 200 and direction < 0:
            self.camera_shift = 7
            self.player.speed = 0
        elif x > 1000 and direction > 0:
            self.camera_shift = -7
            self.player.speed = 0
        else: 
            self.camera_shift = 0
            self.player.speed = 7
