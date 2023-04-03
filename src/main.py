import pygame, sys
from level import Level

level_map = ['00000000000000000000',
             '00000000000000000000',
             '00000000000000000000',
             'xxx00000000000000000',
             'xxx000000P0000000xxx',
             '0000000xxxxx00000xxx',
             '0000000xxxxx00000xxx',
             'xxxxx000000000000000',
             'xxxxxxxx000000xxxxxx']

CELL_SIZE = 64

def main():
    display_height = CELL_SIZE * len(level_map)
    display_width = 1200
    display = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption("Jumpman")
    pygame.init()
    clock = pygame.time.Clock()
    level = Level(level_map)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        display.fill("black")
        level.all_sprites.draw(display)
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()