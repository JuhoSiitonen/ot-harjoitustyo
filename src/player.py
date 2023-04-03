import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((32, 64))
        self.image.fill("green")
        self.rect = self.image.get_rect(topleft = pos)

    def movement(self, dx=0, dy=0):
        self.rect.move_ip(dx, dy)

