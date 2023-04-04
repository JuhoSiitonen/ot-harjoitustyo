import pygame

class Clock:
    def __init__(self):
        self.clock = pygame.time.Clock()

    def tick(self):
        self.clock.tick(60)