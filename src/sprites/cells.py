import pygame


class Cell(pygame.sprite.Sprite):
    """Class to handle sprites in the pygame window, inherits from the pygame sprite
    class.

    Attributes:
        image: Creates a surface object with dimensions defined in the parameters. 
        color: String which is used to tell pygame the color of the created sprite.
        rect: Rectangle which is bound to the sprite created, it has the sprites 
        dimensions and the rect can be interacted with. 
    """

    def __init__(self, pos, size_y, size_x, color):
        """Constructor for the class, initializes an instance of the sprite class
        from which the Cell class inherits from. 

        Args:
            pos (tuple(int,int)): X and y coordinates for the topleft corner of the 
            sprite to be created.
            size_y (int): Dimension for the sprite in y axis.
            size_x (int): Dimension for the sprite in x axis.
            color (str): String to tell pygame the color of the sprite.
        """

        super().__init__()
        self.image = pygame.Surface((size_y, size_x))
        self.color = color
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_dx):
        """Update method to update the sprites position by adding to the x coordinate
        value. This is used to shift screen if player moves to the side.

        Args:
            x_dx (int): The change in x value which sprite needs to be shifted.
        """
        
        self.rect.x += x_dx
