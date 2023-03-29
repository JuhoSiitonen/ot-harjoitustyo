import pygame
from cells import Cell

class Level:
    def __init__(self, level_map, surface):
        self.display_surface = surface
        self.setup(level_map)

    def setup(self,layout):
        self.cells = pygame.sprite.Group()
        for row_index, row in enumerate(layout):
            for col_index, col in enumerate(row):
                if col == "x":
                    x = col_index * 64
                    y = row_index * 64
                    cell = Cell((x,y),64)
                    self.cells.add(cell)

    def run(self):
        self.cells.draw(self.display_surface)