import pygame
from cells import Cell
from player import Player

class Level:
    def __init__(self, level_map):
        self.setup(level_map)
        self.camera_shift = 0

    def setup(self, level_map):
        self.cells = pygame.sprite.Group()
        self.player_cell = pygame.sprite.GroupSingle()
        self.goal = pygame.sprite.GroupSingle()
        self.all_sprites = pygame.sprite.Group()
        for row_index, row in enumerate(level_map):
            for col_index, col in enumerate(row):
                x = col_index * 64 # pylint: disable=invalid-name
                y = row_index * 64 # pylint: disable=invalid-name
                if col == "x":
                    self.cell = Cell((x, y), 64, "white")
                    self.cells.add(self.cell)
                if col == "P":
                    self.player = Player((x, y))
                    self.player_cell.add(self.player)
                if col == "G":
                    self.goal_cell = Cell((x,y), 64, "blue")
                    self.goal.add(self.goal_cell)
        self.all_sprites.add(
            self.cells,
            self.player_cell,
            self.goal
        )

    def camera(self):
        x = self.player.get_player_x() # pylint: disable=invalid-name
        direction = self.player.get_direction()
        if x < 200 and direction < 0:
            self.camera_shift = 7
            self.player.speed = 0
        elif x > 1000 and direction > 0:
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
