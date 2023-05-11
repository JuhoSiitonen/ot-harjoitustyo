import pygame


class Player(pygame.sprite.Sprite):
    """Class to handle player sprite, has all the player movement methods.

    Args:
        pygame (object): Sprite object
    """

    def __init__(self, pos):
        """Class contructor, inherits from the pygame.sprite.Sprite class
        and it gives this class many methods to deal with collisions.

        Args:
            pos (tuple): x and y coordinates for sprite topleft corner.
        """

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
        """Method to handle the sprites movement in x coordinates. Calls
        movement method to actually change sprite position.
        """

        change = self.direction.x * self.speed
        self.movement(dx=change)

    def apply_gravity(self):
        """Method to pull player sprite towards "ground" and thus creating a
        sense of gravity in the game. Calls movement method to actually change 
        sprite position. 
        """

        self.direction.y += self.gravity
        self.movement(dy=self.direction.y)

    def jump(self):
        """Method to facilitate player sprite jump mechanic, player can only jump if it is on 
        ground and its y directional speed is 0.
        """

        if self.direction.y == 0:
            self.direction.y = self.jump_speed

    def movement(self, dx=0, dy=0): # pylint: disable=invalid-name
        """Method to actually move the player sprite in x and y coordinates.

        Args:
            dx (int): Player sprite position change in x axis. Defaults to 0.
            dy (int): Player sprite position change in y axis. Defaults to 0.
        """

        self.rect.move_ip(dx, dy)

    def get_player_x(self):
        """Method to let level class access player x coordinate.

        Returns:
            int: x coordinate value
        """
        return self.rect.x

    def get_direction(self):
        """Method to let level class access player direction. 

        Returns:
            int : -1 is direction to left, and +1 to right.
        """
        
        return self.direction.x
