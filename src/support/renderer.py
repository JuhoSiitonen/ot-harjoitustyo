import pygame
import time

class Renderer:
    def __init__(self, display, level, time_attack):
        self.display = display
        self.level = level
        self.time_attack = time_attack
        self.start = time.time()

    def counter_text(self, count, color, placement):
        fontt = pygame.font.SysFont("Arial", 40)
        counter = fontt.render(f"{count}", True, color)
        self.display.blit(counter, placement)

    def time_counter(self):
        if self.time_attack:
            counter = round((time.time() - self.start), 2)
            self.counter_text(counter, "white", (100, 25))

    def render(self):
        self.display.fill("black")
        self.level.all_sprites.update(self.level.camera_shift)
        self.level.all_sprites.draw(self.display)
        self.counter_text(self.level.player.coins, "yellow", (1100, 25))
        self.counter_text(self.level.player.artifacts, "red", (1100, 70))
        self.time_counter()
        pygame.display.update()
        self.level.camera()
