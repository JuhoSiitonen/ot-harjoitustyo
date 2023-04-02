import pygame
from cells import Cell
from player import Player

class Level:
    def __init__(self, level_map, surface):
        self.display_surface = surface
        self.setup(level_map)
        self.camera_shift = 0

    def setup(self,layout):
        self.cells = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        for row_index, row in enumerate(layout):
            for col_index, col in enumerate(row):
                x = col_index * 64
                y = row_index * 64
                if col == "x":
                    cell = Cell((x,y),64)
                    self.cells.add(cell)
                if col == "P":
                    player_cell = Player((x,y))
                    self.player.add(player_cell)

    def run(self):
        self.cells.update(self.camera_shift)
        self.cells.draw(self.display_surface)
        self.player.draw(self.display_surface)