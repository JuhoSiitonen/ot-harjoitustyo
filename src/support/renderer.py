import pygame

class Renderer:
    def __init__(self, display, level):
        self.display = display
        self.level = level

    def render(self):
        self.display.fill("black")
        self.level.all_sprites.update(self.level.camera_shift)
        self.level.all_sprites.draw(self.display)
        coin_font = pygame.font.SysFont("Arial", 45)
        coin_count = coin_font.render(f"{self.level.player.coins}", True, "yellow")
        self.display.blit(coin_count, (1050, 50))
        pygame.display.update()
        self.level.camera()
