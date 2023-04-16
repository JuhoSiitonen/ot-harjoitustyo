import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((32, 64))
        self.image.fill("green")
        self.rect = self.image.get_rect(topleft=pos)
        
        # Player movement
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 7
        self.gravity = 0.7
        self.jump_speed = -15

    def input(self):
        inputs = pygame.key.get_pressed()
        if inputs[pygame.K_RIGHT]:
            self.direction.x = 1
        elif inputs[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if inputs[pygame.K_SPACE]:
            self.jump()

        change = self.direction.x * self.speed
        self.movement(dx=change)
    
    def apply_gravity(self):
        self.direction.y += self.gravity
        self.movement(dy=self.direction.y)

    def jump(self):
        self.direction.y = self.jump_speed

    def movement(self, dx=0, dy=0):
        self.rect.move_ip(dx, dy)

    def get_player_x(self):
        return self.rect.x
    
    def get_direction(self):
        return self.direction.x