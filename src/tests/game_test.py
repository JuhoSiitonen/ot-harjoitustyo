import unittest
import pygame
from logic.level import Level
from logic.game import Game

class StubDB:
    def insert_into_highscores(level_number, counter):
        pass

class StubClock:
    def tick(self):
        pass

class StubKey_press:
    def __init__(self, key):
        self.key = key
    
    def get(self):
        pressed = {pygame.K_RIGHT : False, pygame.K_LEFT : False, 
                   pygame.K_SPACE : False}
        pressed[self.key] = True
        return pressed

class StubEvent:
    def __init__(self, event_type, key):
        self.type = event_type
        self.key = key

class StubEvent_handling:
    def __init__(self, events, key_pressed):
        self.events = events
        self.pressed = key_pressed

    def get(self):
        return self.events
    
    def get_pressed(self):
        return self.pressed
    
class StubRenderer:
    def __init__(self):
        self.timeout = False

    def render(self):
        pass

level_map = ['00000000000000000000',
             '00000000000000000000',
             '00000000000000000000',
             'xxx000000x0000000000',
             'xxx0000BEPGB00000xxx',
             '0000000xxxxx00000xxx',
             '0000000xxxxx00000xxx',
             'xxxxx000000000000000',
             'xxxxxxxx000000xxxxxx']

class TestGameLoop(unittest.TestCase):
    def setUp(self):
        self.level = Level(level_map, False)
        self.level_number = 1

    def test_game_can_complete_level(self):
        pressed = StubKey_press(pygame.K_RIGHT).get()
        events = [
            StubEvent(pygame.KEYDOWN, pygame.K_LEFT),
        ]
        game = Game(
            self.level,
            StubClock(),
            StubEvent_handling(events, pressed),
            StubRenderer(),
            self.level_number,
            StubDB()
        )
        game.start()
        self.assertEqual(self.level.level_completion(), True)

    def test_game_window_closed(self):
        pressed = StubKey_press(pygame.K_LEFT).get()
        events = [
            StubEvent(pygame.QUIT, None),
        ]
        game = Game(
            self.level,
            StubClock(),
            StubEvent_handling(events, pressed),
            StubRenderer(),
            self.level_number,
            StubDB()
        )
        game.start()
        self.assertEqual(game.handle_events(), False)

    def test_player_demise_works(self):
        pressed = StubKey_press(pygame.K_LEFT).get()
        events = [
            StubEvent(pygame.QUIT, None),
        ]
        game = Game(
            self.level,
            StubClock(),
            StubEvent_handling(events, pressed),
            StubRenderer(),
            self.level_number,
            StubDB()
        )   
        game.start()
        player = self.level.sprites.player_cell.sprite
        x_value = player.rect.x
        for enemy in self.level.sprites.enemies:
            enemy.rect.x = x_value 
        self.assertEqual(self.level.player_demise(), True)
        pygame.quit()

    


