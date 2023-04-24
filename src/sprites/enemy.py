import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, size_y, size_x, color):
        super().__init__()
        self.image = pygame.Surface((size_y, size_x))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = -1
        self.speed = 4

    def update(self, x_dx):
        self.rect.x += x_dx
