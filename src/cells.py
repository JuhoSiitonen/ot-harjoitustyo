import pygame


class Cell(pygame.sprite.Sprite):
    def __init__(self, pos, size_y, size_x, color):
        super().__init__()
        self.image = pygame.Surface((size_y, size_x))
        self.color = color
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_dx):
        self.rect.x += x_dx
