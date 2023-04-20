import pygame

class Renderer:
    def __init__(self, display, level):
        self.display = display
        self.level = level

    def render(self):
        self.display.fill("black")
        self.level.cells.update(self.level.camera_shift)
        self.level.goal.update(self.level.camera_shift)
        self.level.all_sprites.draw(self.display)
        pygame.display.update()
        self.level.camera()
