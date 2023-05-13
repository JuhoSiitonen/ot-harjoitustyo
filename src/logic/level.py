import time
from sprites.sprite_handler import SpriteHandler
from settings import CELL_SIZE

class Level:
    """Class to setup sprites to screen from a level data list. Also
    handles collision checks and the rolling camera. 

    Attributes:
        sprites: SpriteHandler object to initialize sprites.
        level_map: Nested list with level information, which is used
            to create level with setup method.
        camera_shift: Integer value for "camera" movement speed, actually 
            the display doesn't move, all the sprites move instead. 
        level_number: Integer value to identify level.
    """

    def __init__(self, level_map, level_number):
        """Class constructor which calls a method to initialize sprite 
        groups and then sets up the level from level_map list data, also 
        keeps level number info. 

        Args:
            level_map (list): List with level data.
            level_number (int): Levels identifying integer.
        """

        self.sprites = SpriteHandler()
        self.level_map = level_map
        self.setup()
        self.camera_shift = 0
        self.level_number = level_number
        self.start = time.time()
        self.counter = 1

    def setup(self):
        """Method to enumerate level_map data and instantiate appropriate 
        sprite classes by calling sprite_handler class methods to do it. 
        """

        for row_index, row in enumerate(self.level_map):
            for col_index, col in enumerate(row):
                x_coord = col_index * CELL_SIZE
                y_coord = row_index * CELL_SIZE
                if col == " ":
                    continue
                if col == "P":
                    self.sprites.player_sprite_creator(x_coord,y_coord)
                elif col == "E":
                    self.sprites.enemy_sprite_creator(x_coord,y_coord)
                else:
                    self.sprites.sprite_creator(col, x_coord, y_coord)
        self.sprites.collect_sprites_to_all_sprites()

    def re_initialize(self):
        """Method to re initialize level sprites to their original positions, and thus return 
        to the beginning of the level. Used in case player sprite collides with enemy, or falls
        off screen. 
        """

        self.sprites = SpriteHandler()

    def camera(self):
        """Method to move display (camera) according to player movement.
        """

        x_coord = self.sprites.player.get_player_x()
        direction = self.sprites.player.get_direction()
        if x_coord < 300 and direction < 0:
            self.camera_shift = 7
            self.sprites.player.speed = 0
        elif x_coord > 900 and direction > 0:
            self.camera_shift = -7
            self.sprites.player.speed = 0
        else:
            self.camera_shift = 0
            self.sprites.player.speed = 7

    def horizontal_collision(self):
        """Method to check player horizontal collisions and return player 
        sprite to appropriate side of obstacle.
        """

        player = self.sprites.player_cell.sprite
        for sprite in self.sprites.cells.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def vertical_collision(self):
        """Method to check player vertical collisions and return player 
        sprite to appropriate side of obstacle.
        """

        player = self.sprites.player_cell.sprite
        for sprite in self.sprites.cells.sprites():
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

        player = self.sprites.player_cell.sprite
        for sprite in self.sprites.coins.sprites():
            if sprite.rect.colliderect(player.rect):
                sprite.kill()
                self.sprites.player.coins += 1

    def artifact_collision(self):
        """Method to check if player hits artifact, and adds it to artifact 
        count simultaneously destroying the artifact sprite from screen.
        """

        player = self.sprites.player_cell.sprite
        for sprite in self.sprites.artifacts.sprites():
            if sprite.rect.colliderect(player.rect):
                sprite.kill()
                self.sprites.player.artifacts += 1

    def level_completion(self):
        """Method to check if player hits level goal and completes level.

        Returns:
            bool: False continues gameplay, True ends game class loop.
        """

        player = self.sprites.player_cell.sprite
        if self.sprites.goal_cell.rect.colliderect(player.rect):
            return True
        return False

    def player_demise(self):
        """Method to check if player collides with enemy or falls 
        off screen, in case that happens, returns player to starting 
        position by re initializing the level sprites.

        Returns:
            bool: True re initializes level, False continues gameplay.
        """

        player = self.sprites.player_cell.sprite
        if player.rect.y > len(self.level_map) * CELL_SIZE + 100:
            return True
        for sprite in self.sprites.enemies.sprites():
            if sprite.rect.colliderect(player.rect):
                return True
        return False

    def enemy_movement(self):
        """Method to check if enemy sprites collide with invisible blocker
        sprites, which cause the enemy sprites direction to change.
        """

        for enemy in self.sprites.enemies:
            for sprite in self.sprites.blocker.sprites():
                if sprite.rect.colliderect(enemy.rect):
                    enemy.direction *= -1
            enemy.update((enemy.speed*enemy.direction))

    def update(self):
        """Method to call other methods from level class and also player class
        to check all collisions, update timer, and move player.
        """

        self.sprites.player.move()
        self.horizontal_collision()
        self.sprites.player.apply_gravity()
        self.vertical_collision()
        self.coin_collision()
        self.artifact_collision()
        self.enemy_movement()
