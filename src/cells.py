import pygame


class Cell(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill("white")
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_dx):
        self.rect.x += x_dx
