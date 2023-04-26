import pygame

class Renderer:
    def __init__(self, display, level):
        self.display = display
        self.level = level

    def counter_text(self, count, color, placement):
        fontt = pygame.font.SysFont("Arial", 40)
        counter = fontt.render(f"{count}", True, color)
        self.display.blit(counter, placement)

    def render(self):
        self.display.fill("black")
        self.level.all_sprites.update(self.level.camera_shift)
        self.level.all_sprites.draw(self.display)
        self.counter_text(self.level.player.coins, "yellow", (1100, 25))
        self.counter_text(self.level.player.artifacts, "red", (1100, 70))
        pygame.display.update()
        self.level.camera()
