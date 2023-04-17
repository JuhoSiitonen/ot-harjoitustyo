import pygame


class EventHandling:
    def __init__(self):
        pass

    def get(self):
        return pygame.event.get()

    def get_pressed(self):
        return pygame.key.get_pressed()
