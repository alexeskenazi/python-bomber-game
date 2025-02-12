from src.game_screen import GameScreen
from src.game_controller import GameController
from src.display import Display
from src.game_model import GameModel


class Game:
    '''
    Game object - holds the games movel, view, and controllers
    '''

    def __init__(self, display: Display) -> None:
        '''
        constructor
        display: (Display) object containing the display information.
        '''
        self.game_model = GameModel()
        self.game_controller = GameController(self.game_model)
        self.game_screen = GameScreen(display, self.game_model)

    def start(self):
        '''
        Starts the game.
        '''
        self.game_model.start_game()

    def hangle_event(self, events):
        '''
        Handls the user input during the game
        '''
        self.game_controller.handle_game_events(events)

    def update_data(self):
        '''
        Updates the game data/model.
        '''
        return self.game_model.update_data()

    def draw(self):
        '''
        Draws the game on the screen
        '''
        self.game_screen.draw()

    def is_over(self) -> bool:
        '''
        Checks whether the game is over
        return: (bool) True if game is over
        '''
        return self.game_model.is_over
