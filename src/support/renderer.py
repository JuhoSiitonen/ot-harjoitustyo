import pygame

class Renderer:
    """Class to render the Pygame screen with the sprites initialized by the level
    object.

    Attributes: 
        display: The surface which pygame is rendered on.
        level: Level object which initializes the sprites and handles their interactions.
        time_attack: Boolean to tell if time attack mode is chosen. 
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

    def time_counter(self, counter):
        """If time attack mode is chosen calls counter_text method to draw time left
        on pygame window.
        """

        if self.time_attack:
            self.counter_text(counter, "white", (100, 25))

    def update(self):
        """Method to fill pygame display surface with a black color first, then 
        update the sprites placement with a camera shift value from level object
        and then draw them to the surface. Followed by drawing the coin and artifact
        counters.Then it calls level.camera to update camera shift value. 
        """

        self.display.fill("black")
        self.level.sprites.all_sprites.update(self.level.camera_shift)
        self.level.sprites.all_sprites.draw(self.display)
        self.counter_text(self.level.sprites.player.coins, "yellow", (1100, 25))
        self.counter_text(self.level.sprites.player.artifacts, "red", (1100, 70))
        self.level.camera()


    def render(self):
        """Method to actually update the display for the user
        """

        pygame.display.update()
