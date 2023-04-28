import pygame


class EventHandling:
    """Class to handle pygame events and inputs.
    """

    def __init__(self):
        """Constructor for the class
        """

        pass

    def get(self):
        """Method to send pygame events to calling class, mainly used to check if
        player exits the window.

        Returns:
            dict: Returns an event_type and key value. Such as pygame.KEYDOWN : 
            pygame.K_LEFT.
        """

        return pygame.event.get()

    def get_pressed(self):
        """Method to send pygame inputs to calling class. 

        Returns:
            dict: Keys are the keyboard keys and values are booleans to describe if
            said key is pressed.  
        """
        
        return pygame.key.get_pressed()
