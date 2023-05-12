import pygame

class Game:
    """Class to handle Pygame loop by checking events, inputs and updating the 
    level object which is rendered by the render object with a framerate defined by 
    the clock object.

    Attributes:
        level: Level object which handles sprites and their interactions in the 
        rendered level.
        clock: Clock object which refreshes the Pygame window 60 time a second.
        even_handling: Event_handling object which sends the Pygame events and inputs
        to this class.
        renderer: Renderer object which handles rendering the Pygame screen with sprites
        and text.
        level_number: Integer to help call highscore database insertion after time attack 
        level completion.
        hs_rep: Highscore_Repository object to interact with highscore database.
    """

    def __init__(self, level, clock, event_handling, renderer, level_number, hs_rep):
        """Constructor for the class, connects the injected dependencies to this 
        instance of game class.

        Args:
            level (object): Level object which handles sprites and their interactions in the 
            rendered level.
            clock (object): Clock object which refreshes the Pygame window 60 time a second.
            event_handling (object): Event_handling object which sends the Pygame events and 
            inputs to this class.
            renderer (object): Renderer object which handles rendering the Pygame screen 
            with sprites and text.
            level_number (int): Integer to help call highscore database insertion after time attack 
            level completion.
            hs_rep (object): Highscore_Repository object to interact with highscore database.
        """

        self.level_number = level_number
        self.level = level
        self.clock = clock
        self.event_handling = event_handling
        self.renderer = renderer
        self.highscore_repository = hs_rep

    def handle_events(self):
        """Method to handle Pygame events by calling the event_handling object.

        Returns:
            Bool: If true the player has not exited the Pygame window, if false the
            window is closed and a return to the UI window ensues. 
        """

        for event in self.event_handling.get():
            if event.type == pygame.QUIT:
                return False
        return True

    def handle_inputs(self):
        """Method to handle inputs via the event_handling object. Changes player 
        class objects direction according to keyboard arrow presses and spacebar
        calls the player classes jump method to make player jump.
        """

        inputs = self.event_handling.get_pressed()
        if inputs[pygame.K_RIGHT]:
            self.level.sprites.player.direction.x = 1
        elif inputs[pygame.K_LEFT]:
            self.level.sprites.player.direction.x = -1
        else:
            self.level.sprites.player.direction.x = 0
        if inputs[pygame.K_SPACE]:
            self.level.sprites.player.jump()

    def start(self):
        """Start the games main loop which checks events for window closing, checks
        if the player has finished the level, checks if player dies and then re-
        initializes the level object sprites and returns to the start of the level. 
        Method then calls handle_inputs to move player, level objects update method to
        update sprites and check collisions, then render method to render the screen and
        clock object to refresh the screen at a certain framerate. If loop is exited by
        completing level or exiting Pygame window it quits pygame to return to UI window.
        """

        running = True
        while running:
            if not self.handle_events():
                running = False
            if self.level.level_completion():
                if self.level.time_attack:
                    self.write_highscore_to_db(self.level_number,self.level.counter)
                running = False
            if self.level.player_demise() is True:
                self.level.re_initialize()
                self.level.setup()
            self.handle_inputs()
            self.level.update()
            self.render()
            self.clock.tick()
        pygame.quit()

    def render(self):
        """Calls renderer object to render the pygame screen.
        """

        self.renderer.render()

    def write_highscore_to_db(self, level_number, counter):
        """Method to call database repository object for insertion into
        the highscore database. 15 seconds is the max completion time which is shown 
        on the screen running down, so to insert the actual completion time to database
        we need to do the calculation (15 - counter).

        Args:
            level_number (int): Integer to tell which level was completed.
            counter (float): Time left in counter after level completion.
        """

        time = round(15 - counter, 2)
        self.highscore_repository.insert_into_highscores(level_number,time)
