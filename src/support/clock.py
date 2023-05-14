import time
import pygame


class Clock:
    """Class to handle framerate in pygame. Used also to check 
    starting time of gameplay for time attack mode.
    """

    def __init__(self):
        """Constructor for the class.

        Attributes:
            clock: Pygame clock object which has a tick method used for framerate handling.
        """

        self.clock = pygame.time.Clock()

    def tick(self):
        """Method to call pygame.clock objects tick method and handle framerate.
        """

        self.clock.tick(60)

    def time_now(self):
        """Method to give time attack mode the starting time.

        Returns:
            float: timestamp.
        """
        return time.time()
