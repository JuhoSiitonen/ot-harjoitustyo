import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((32, 64))
        self.image.fill("green")
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 7

    def input(self):
        inputs = pygame.key.get_pressed()
        if inputs[pygame.K_RIGHT]:
            self.direction.x = 1
        elif inputs[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0
        change = self.direction.x * self.speed
        self.movement(dx=change)

    def movement(self, dx=0, dy=0):
        self.rect.move_ip(dx, dy)

    def get_player_x(self):
        return self.rect.x
    
    def get_direction(self):
        return self.direction.x