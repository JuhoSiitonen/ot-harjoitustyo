import pygame

class Game:
    def __init__(self, level, clock, event_handling, renderer):
        self.level = level
        self.clock = clock
        self.event_handling = event_handling
        self.renderer = renderer

    def handle_events(self):
        for event in self.event_handling.get():
            if event.type == pygame.QUIT:
                return False
        return True

    def handle_inputs(self):
        inputs = self.event_handling.get_pressed()
        if inputs[pygame.K_RIGHT]:
            self.level.player.direction.x = 1
        elif inputs[pygame.K_LEFT]:
            self.level.player.direction.x = -1
        else:
            self.level.player.direction.x = 0

        if inputs[pygame.K_SPACE]:
            self.level.player.jump()

        self.level.update()

    def start(self):
        running = True
        while running:
            if self.handle_events() is False:
                running = False
            if self.level.level_completion() is True:
                running = False
            self.handle_inputs()
            self.render()
            self.clock.tick()
        pygame.quit()

    def render(self):
        self.renderer.render()
