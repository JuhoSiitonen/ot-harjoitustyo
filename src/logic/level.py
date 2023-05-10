import time
import pygame
from sprites.cells import Cell
from sprites.player import Player
from sprites.enemy import Enemy
from settings import DISPLAY_HEIGHT, CELL_SIZE

class Level:
    """Class to setup sprites to screen from a level data list. Also
    handles collision checks and the rolling camera. 
    """

    def __init__(self, level_map, time_attack):
        """Class constructor which calls a method to initialize sprite 
        groups and then sets up the level from level_map list data. If 
        time attack mode is chosen, begins timer. 

        Args:
            level_map (list): List with level data.
            time_attack (bool): Signals time_counter function to count time.
        """

        self.level_map = level_map
        self.initialize_sprite_groups()
        self.setup()
        self.camera_shift = 0
        self.time_attack = time_attack
        self.start = time.time()
        self.counter = 1

    def initialize_sprite_groups(self):
        """Initializes sprite groups
        """

        self.cells = pygame.sprite.Group()
        self.player_cell = pygame.sprite.GroupSingle()
        self.goal = pygame.sprite.GroupSingle()
        self.enemies = pygame.sprite.Group()
        self.blocker = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.artifacts = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

    def _sprite_creator(self, type, X, Y):
        """Instantiates sprites which belong to Cell class.

        Args:
            type (str): To tell which sprite is created.
            x (int): Coordinate value for sprite topleft corner.
            y (int): Coordinate value for sprite topleft corner.
        """

        if type == "x":
            self.cell = Cell((X, Y), 64, 64, "white")
            self.cells.add(self.cell)
        elif type == "G":
            self.goal_cell = Cell((X,Y), 32, 64, "blue")
            self.goal.add(self.goal_cell)
        elif type == "B":
            self.blocker_cell = Cell((X,Y), 64, 64, "black")
            self.blocker.add(self.blocker_cell)
        elif type == "C":
            self.coin_cell = Cell((X,Y), 24, 24, "yellow")
            self.coins.add(self.coin_cell)
        elif type == "A":
            self.artifact_cell = Cell((X,Y), 24, 24, "red")
            self.artifacts.add(self.artifact_cell)

    def _collect_sprites_to_all_sprites(self):
        """After level data is read and sprites created, adds all 
        sprites to one group for easier camera movement.
        """

        self.all_sprites.add(
            self.blocker,
            self.coins,
            self.artifacts,
            self.cells,
            self.player_cell,
            self.goal,
            self.enemies
        )

    def setup(self):
        """Method to enumerate level_map data and instantiate appropriate 
        sprite classes. 
        """

        for row_index, row in enumerate(self.level_map):
            for col_index, col in enumerate(row):
                X = col_index * CELL_SIZE # pylint: disable=invalid-name
                Y = row_index * CELL_SIZE # pylint: disable=invalid-name
                if col == " ":
                    continue
                if col == "P":
                    self.player = Player((X, Y))
                    self.player_cell.add(self.player)
                elif col == "E":
                    self.enemy_cell = Enemy((X,Y), 32, 64, "red")
                    self.enemies.add(self.enemy_cell)
                else:
                    self._sprite_creator(col, X, Y)
        self._collect_sprites_to_all_sprites()

    def camera(self):
        """Method to move display (camera) according to player movement.
        """

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
        """Method to check player horizontal collisions and return player 
        sprite to appropriate side of obstacle.
        """

        player = self.player_cell.sprite
        for sprite in self.cells.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def vertical_collision(self):
        """Method to check player vertical collisions and return player 
        sprite to appropriate side of obstacle.
        """

        player = self.player_cell.sprite
        for sprite in self.cells.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                elif player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0

    def coin_collision(self):
        """Method to check if player hits coin, and adds it to coin count
        simultaneously destroying the coin sprite from screen.
        """

        player = self.player_cell.sprite
        for sprite in self.coins.sprites():
            if sprite.rect.colliderect(player.rect):
                sprite.kill()
                self.player.coins += 1

    def artifact_collision(self):
        """Method to check if player hits artifact, and adds it to artifact 
        count simultaneously destroying the artifact sprite from screen.
        """

        player = self.player_cell.sprite
        for sprite in self.artifacts.sprites():
            if sprite.rect.colliderect(player.rect):
                sprite.kill()
                self.player.artifacts += 1

    def level_completion(self):
        """Method to check if player hits level goal and completes level,
        also check if time runs out. If time runs out exits level.

        Returns:
            bool: False continues gameplay, True ends game class loop.
        """

        player = self.player_cell.sprite
        if self.goal_cell.rect.colliderect(player.rect):
            return True
        if self.counter < 0.01:
            return True
        return False

    def player_demise(self):
        """Method to check if player collides with enemy or falls 
        off screen, in case that happens, returns player to starting 
        position by re initializing the level sprites.

        Returns:
            bool: True re initializes level, False continues gameplay.
        """

        player = self.player_cell.sprite
        if player.rect.y > DISPLAY_HEIGHT + 100:
            return True
        for sprite in self.enemies.sprites():
            if sprite.rect.colliderect(player.rect):
                return True
        return False

    def enemy_movement(self):
        """Method to check if enemy sprites collide with invisible blocker
        sprites, which cause the enemy sprites direction to change.
        """

        for enemy in self.enemies:
            for sprite in self.blocker.sprites():
                if sprite.rect.colliderect(enemy.rect):
                    enemy.direction *= -1
            enemy.update((enemy.speed*enemy.direction))

    def time_counter(self):
        """If time attack mode is chosen this method calculates time left from the
        starting timestamp self.start.
        """

        if self.time_attack:
            self.counter = round((15.0 - (time.time() - self.start)), 2)

    def update(self):
        """Method to call other methods from level class and also player class
        to check all collisions, update timer, and move player.
        """

        self.time_counter()
        self.player.move()
        self.horizontal_collision()
        self.player.apply_gravity()
        self.vertical_collision()
        self.coin_collision()
        self.artifact_collision()
        self.enemy_movement()
