import pygame
import time

class Renderer:
    """Class to render the Pygame screen with the sprites initialized by the level
    object.

    Attributes: 
        display: The surface which pygame is rendered on.
        level: Level object which initializes the sprites and handles their interactions.
        time_attack: Boolean to tell if time attack mode is chosen. 
        start: Starting timestamp for time attack mode. 
    """

    def __init__(self, display, level, time_attack):
        """Constructs the rendered class with injected depency on level class,
        created display for pygame and the information whether time attack mode
        has been chosen. 

        Args:
            display (object): The surface which pygame is rendered on.
            level (object): Level object which initializes the sprites and handles 
            their interactions.
            time_attack (bool): Boolean to tell if time attack mode is chosen. 
        """

        self.display = display
        self.level = level
        self.time_attack = time_attack
        self.start = time.time()

    def counter_text(self, count, color, placement):
        """Method which uses blit to draw text to the pygame window. 

        Args:
            count (str): String which is drawn on the screen.
            color (str): String to define text color to pygame.
            placement (tuple(int, int)): Integer tuple to define x and y values where
            to draw text. 
        """

        fontt = pygame.font.SysFont("Arial", 40)
        counter = fontt.render(f"{count}", True, color)
        self.display.blit(counter, placement)

    def time_counter(self):
        """If time attack mode is chosen this method calculates time left from the
        starting timestamp self.start and calls counter_text method to draw time left
        on pygame window.
        """

        if self.time_attack:
            counter = round((15.0 - (time.time() - self.start)), 2)
            self.counter_text(counter, "white", (100, 25))

    def render(self):
        """Method to fill pygame display surface with a black color first, then 
        update the sprites placement with a camera shift value from level object
        and then draw them to the surface. Followed by drawing the coin, artifact
        and in case time attack mode has been chosen the time left to the window.
        Then it updates the pygame window with this information and calls level.camera.
        To update camera shift value. 
        """
        
        self.display.fill("black")
        self.level.all_sprites.update(self.level.camera_shift)
        self.level.all_sprites.draw(self.display)
        self.counter_text(self.level.player.coins, "yellow", (1100, 25))
        self.counter_text(self.level.player.artifacts, "red", (1100, 70))
        self.time_counter()
        pygame.display.update()
        self.level.camera()
