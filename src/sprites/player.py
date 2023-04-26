import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((32, 64))
        self.image.fill("green")
        self.rect = self.image.get_rect(topleft=pos)

        self.direction = pygame.math.Vector2(0,0)
        self.speed = 7
        self.gravity = 0.7
        self.jump_speed = -15
        self.coins = 0
        self.artifacts = 0

    def move(self):
        change = self.direction.x * self.speed
        self.movement(dx=change)

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.movement(dy=self.direction.y)

    def jump(self):
        if self.direction.y == 0:
            self.direction.y = self.jump_speed

    def movement(self, dx=0, dy=0): # pylint: disable=invalid-name
        self.rect.move_ip(dx, dy)

    def get_player_x(self):
        return self.rect.x

    def get_direction(self):
        return self.direction.x
