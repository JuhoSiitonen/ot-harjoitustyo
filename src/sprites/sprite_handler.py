import pygame
from sprites.cells import Cell
from sprites.player import Player
from sprites.enemy import Enemy

class SpriteHandler:
    """Class to handle instantiation of sprites. Class methods create sprites from either cell, 
    player or enemy class. The instantiated sprite objects are also added to pygame sprite groups
    to be able to update all of the same kind of sprites with one command. 

    Attributes:
        cells : Most generic sprites are the cell class sprites, they have only an update method, 
        and can be modified with the class instantiation args.
        player_cell: Player sprite which has methods for movement in the screen.
        goal: The level goal sprite, generic cell class sprite.
        enemies: Enemy sprites, have an update method and direction and speed variables.
        blocker: Generic cell class sprites which are invisible to the player, intended to block
            enemy sprites from moving out of the screen.
        coins: Generic cell class sprites.
        aritfacts: Generic cell class sprites.
        all_sprites: Sprite group to control all sprites at once.
    """

    def __init__(self):
        """Class constructor which creates all the necessary sprite groups.
        """

        self.cells = pygame.sprite.Group()
        self.player_cell = pygame.sprite.GroupSingle()
        self.goal = pygame.sprite.GroupSingle()
        self.enemies = pygame.sprite.Group()
        self.blocker = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.artifacts = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        self.goal_cell = ""
        self.player = ""
        self.enemy_cell = ""

    def sprite_creator(self, sprite_type, x_coord, y_coord):
        """Instantiates sprites which belong to Cell class.

        Args:
            sprite_type (str): To tell which sprite is created.
            x (int): Coordinate value for sprite topleft corner.
            y (int): Coordinate value for sprite topleft corner.
        """

        if sprite_type == "x":
            cell = Cell((x_coord, y_coord), 64, 64, "white")
            self.cells.add(cell)
        elif sprite_type == "G":
            self.goal_cell = Cell((x_coord,y_coord), 32, 64, "blue")
            self.goal.add(self.goal_cell)
        elif sprite_type == "B":
            blocker_cell = Cell((x_coord,y_coord), 64, 64, "black")
            self.blocker.add(blocker_cell)
        elif sprite_type == "C":
            coin_cell = Cell((x_coord,y_coord), 24, 24, "yellow")
            self.coins.add(coin_cell)
        elif sprite_type == "A":
            artifact_cell = Cell((x_coord,y_coord), 24, 24, "red")
            self.artifacts.add(artifact_cell)

    def player_sprite_creator(self, x_coord, y_coord):
        """Method to instantiate the player class cell. One per level.

        Args:
            X (int): X axis coordinate for cell topleft corner
            Y (int): Y axis coordinate for cell topleft corner
        """

        self.player = Player((x_coord, y_coord))
        self.player_cell.add(self.player)

    def enemy_sprite_creator(self, x_coord, y_coord):
        """Method to instantiate the enemy class cells, can be many per level.

        Args:
            X (int): X axis coordinate for cell topleft corner
            Y (int): Y axis coordinate for cell topleft corner
        """

        self.enemy_cell = Enemy((x_coord,y_coord), 32, 64, "red")
        self.enemies.add(self.enemy_cell)

    def collect_sprites_to_all_sprites(self):
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
