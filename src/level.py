import pygame
from cells import Cell
from player import Player


class Level:
    def __init__(self, level_map):
        self.setup(level_map)
        self.camera_shift = 0

    def setup(self, level_map):
        self.cells = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.all_sprites = pygame.sprite.Group()
        for row_index, row in enumerate(level_map):
            for col_index, col in enumerate(row):
                x = col_index * 64
                y = row_index * 64
                if col == "x":
                    cell = Cell((x, y), 64)
                    self.cells.add(cell)
                if col == "P":
                    player_cell = Player((x, y))
                    self.player.add(player_cell)
        self.all_sprites.add(
            self.cells,
            self.player
        )
