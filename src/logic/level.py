import pygame
from cells import Cell
from player import Player
from enemy import Enemy
from settings import display_height

class Level:
    def __init__(self, level_map):
        self.level_map = level_map
        self.initialize_sprite_groups()
        self.setup()
        self.camera_shift = 0

    def initialize_sprite_groups(self):
        self.cells = pygame.sprite.Group()
        self.player_cell = pygame.sprite.GroupSingle()
        self.goal = pygame.sprite.GroupSingle()
        self.enemies = pygame.sprite.Group()
        self.blocker = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

    def setup(self):
        for row_index, row in enumerate(self.level_map):
            for col_index, col in enumerate(row):
                x = col_index * 64 # pylint: disable=invalid-name
                y = row_index * 64 # pylint: disable=invalid-name
                if col == "x":
                    self.cell = Cell((x, y), 64, 64, "white")
                    self.cells.add(self.cell)
                elif col == "P":
                    self.player = Player((x, y))
                    self.player_cell.add(self.player)
                elif col == "G":
                    self.goal_cell = Cell((x,y), 32, 64, "blue")
                    self.goal.add(self.goal_cell)
                elif col == "E":
                    self.enemy_cell = Enemy((x,y), 32, 64, "red")
                    self.enemies.add(self.enemy_cell)
                elif col == "B":
                    self.blocker_cell = Cell((x,y), 64, 64, "black")
                    self.blocker.add(self.blocker_cell)
        self.all_sprites.add(
            self.blocker,
            self.cells,
            self.player_cell,
            self.goal,
            self.enemies
        )

    def camera(self):
        x = self.player.get_player_x() # pylint: disable=invalid-name
        direction = self.player.get_direction()
        if x < 300 and direction < 0:
            self.camera_shift = 7
            self.player.speed = 0
        elif x > 900 and direction > 0:
            self.camera_shift = -7
            self.player.speed = 0
        else:
            self.camera_shift = 0
            self.player.speed = 7

    def horizontal_collision(self):
        player = self.player_cell.sprite

        for sprite in self.cells.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def vertical_collision(self):
        player = self.player_cell.sprite

        for sprite in self.cells.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                elif player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0

    def level_completion(self):
        player = self.player_cell.sprite
        if self.goal_cell.rect.colliderect(player.rect):
            return True
        return False

    def player_demise(self):
        player = self.player_cell.sprite
        if player.rect.y > display_height + 100:
            return True
        for sprite in self.enemies.sprites():
            if sprite.rect.colliderect(player.rect):
                return True
        return False

    def enemy_movement(self):
        for enemy in self.enemies:
            for sprite in self.blocker.sprites():
                if sprite.rect.colliderect(enemy.rect):
                    enemy.direction *= -1
            enemy.update((enemy.speed*enemy.direction))

    def update(self):
        self.player.apply_gravity()
        self.vertical_collision()
        self.player.move()
        self.horizontal_collision()
        self.enemy_movement()