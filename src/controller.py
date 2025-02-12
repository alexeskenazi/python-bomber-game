import pygame
from src.background import Background
from src.game import Game
from src.logger import Logger
from src.display import Display
from src.gameover_screen import GameoverScreen
from src.welcome_screen import WelcomeScreen


DISPLAY_WIDTH: int = 1000
DISPLAY_HEIGHT: int = 800
NUM_OF_LANES: int = 10
NUM_OF_ROWS: int = 10
FPS = 40

Logger()  # Global looger used during debugging


class Controller:
    '''
    Main application controller
    '''

    def __init__(self):
        '''
        constructor
        '''
        display = self.init_pygame()
        self.background = Background(display)
        self.welcome_screen = WelcomeScreen(display)
        self.game = Game(display)
        self.gameover_screen = GameoverScreen(display)
        self.clock = pygame.time.Clock()
        self._running = True
        self.set_wecome_screen_state()
        self.background.play_sound()

    def mainloop(self):
        '''
        Main application loop for handling events and displaying content
        '''
        # select state loop
        while self._running:
            if self.is_welcome_screen_state():
                self.menuloop()
            elif self.is_game_on_state():
                self.gameloop()
            elif self.is_game_over_screen_state():
                self.gameoverloop()

    def menuloop(self):
        '''
        Welcome screen loop
        '''
        self.welcome_event_loop()
        self.welcome_update_data()
        self.welcome_redraw_screen()

    def gameloop(self):
        '''
        Game loop for handling user events and displaying the game.
        '''
        self.game_event_loop()
        self.game_update_data()
        self.game_redraw()
        self.clock.tick(FPS)

    def gameoverloop(self):
        '''
        Game over screen loop - handles user input and displays instructions
        '''
        self.game_over_event_loop()
        self.game_over_update_data()
        self.game_over_redraw()

    def init_pygame(self) -> Display:
        '''
        Initialized pygame via the Display wrapper
        return: (Display) wrapper around pygame
        '''
        self.display = Display(width=DISPLAY_WIDTH,
                               height=DISPLAY_HEIGHT,
                               num_of_lanes=NUM_OF_LANES)
        return self.display

    def handle_global_keyboard_event(self, event):
        '''
        Handles keyboard events that are available globally in the application.
        '''
        if event.type != pygame.KEYDOWN:
            return
        if event.key in [pygame.K_s]:
            self.background.toggle_sound()
        if event.key in [pygame.K_r]:
            self.game.game_model.reset_max_score()
        if event.key in [pygame.K_g]:
            Logger.is_debug = not Logger.is_debug
        if event.key in [pygame.K_q]:
            self.exit_app()

    def start_game(self):
        '''
        Starts the game
        '''
        self.set_gameon_state()
        self.game.start()

    def end_game(self):
        '''
        Ends the game
        '''
        self.set_gameover_state()

    def handle_global_event(self, event):
        '''
        Handles global input events. For example, applicaiton being closed.
        '''
        self.check_and_quit_app_if_needed(event)
        self.handle_global_keyboard_event(event)

    def check_and_quit_app_if_needed(self, event):
        '''
        Checks if the user chose to quic the app and cleans up.
        '''
        if (event.type == pygame.QUIT):
            self.exit_app()

    def exit_app(self):
        '''
        Exits the application cleanly
        '''
        self._running = False
        pygame.quit()
        raise SystemExit

    def handle_welcome_screen_event(self, event):
        '''
        Handles user input while the welcome screen is visible
        '''
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_SPACE]:
                self.start_game()

    def handle_gameover_event(self, event):
        '''
        Handles user input while the game over  screen is visible
        '''
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_SPACE]:
                self.start_game()

    def welcome_event_loop(self):
        '''
        Performs the event loop for the welcome screen
        '''
        for event in pygame.event.get():
            self.handle_global_event(event)
            self.handle_welcome_screen_event(event)

    def welcome_update_data(self):
        '''
        Updates the welcome screen data
        '''
        # no data to update
        pass

    def welcome_redraw_screen(self):
        '''
        Draws/Redraws the welcome screen
        '''
        self.background.draw()
        self.welcome_screen.draw()
        pygame.display.update()

    def game_event_loop(self):
        '''
        Performs the game event loop
        '''
        for event in pygame.event.get():
            self.handle_global_event(event)
            self.game.hangle_event(event)

    def game_update_data(self):
        '''
        Updates the game screen data
        '''
        self.game.update_data()
        if self.game.is_over():
            self.end_game()

    def game_redraw(self):
        '''
        Draws/Redraws the game screen
        '''
        self.background.draw()
        self.game.draw()
        pygame.display.update()

    def game_over_event_loop(self):
        '''
        Performs the game over event loop
        '''
        for event in pygame.event.get():
            self.handle_global_event(event)
            self.handle_gameover_event(event)

    def game_over_update_data(self):
        '''
        Updates the game over screen data
        '''
        # no data to update
        pass

    def game_over_redraw(self):
        '''
        Draws/Redraws the game over screen
        '''
        self.background.draw()
        self.gameover_screen.draw()
        pygame.display.update()

    def set_wecome_screen_state(self):
        '''
        Sets application state to show the Welcome Screen.
        '''
        self.app_state = 'welcome'

    def set_gameon_state(self):
        '''
        Sets application state to show the Game Screen.
        '''
        self.app_state = 'game-on'

    def set_gameover_state(self):
        '''
        Sets application state to show the Game Over Screen.
        '''
        self.app_state = 'game-over'

    def is_welcome_screen_state(self) -> bool:
        '''
        return: (bool) True if hte curren app state is the welcome screen
        '''
        return self.app_state == 'welcome'

    def is_game_on_state(self) -> bool:
        '''
        return: (bool) True if hte curren app state is that the game is on
        '''
        return self.app_state == 'game-on'

    def is_game_over_screen_state(self) -> bool:
        '''
        return: (bool) True if hte curren app state is the game over screen
        '''
        return self.app_state == 'game-over'
