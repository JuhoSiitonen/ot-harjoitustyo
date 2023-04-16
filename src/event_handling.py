import pygame


class Event_handling:
    def __init__(self):
        pass

    def get(self):
        return pygame.event.get()
    
    def get_pressed(self):
        return pygame.key.get_pressed()
