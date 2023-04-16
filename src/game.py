import pygame

class Game:
    def __init__(self, level, clock, event_handling, renderer):
        self.level = level
        self.clock = clock
        self.event_handling = event_handling
        self.renderer = renderer

    def handle_events(self):
        self.level.player.input()
        self.level.player.apply_gravity()
        for event in self.event_handling.get():
            if event.type == pygame.QUIT:
                return False

    def start(self):
        while True:
            if self.handle_events() == False:
                break
            self.render()
            self.clock.tick()

    def render(self):
        self.renderer.render()