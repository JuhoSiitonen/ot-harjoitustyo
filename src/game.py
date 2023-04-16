import pygame

class Game:
    def __init__(self, level, clock, event_handling, renderer):
        self.level = level
        self.clock = clock
        self.event_handling = event_handling
        self.renderer = renderer

    def handle_events(self):
        for event in self.event_handling.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.level.player.movement(dx=-5)
                if event.key == pygame.K_RIGHT:
                    self.level.player.movement(dx=5)
                if event.key == pygame.K_UP:
                    self.level.player.movement(dy=-15)

            elif event.type == pygame.QUIT:
                return False

    def start(self):
        while True:
            if self.handle_events() == False:
                break
            self.render()
            self.clock.tick()

    def render(self):
        self.renderer.render()