import pygame

from src.game_model import GameModel


class GameController:
    '''
    Game controller - handles the user input during the game
    '''

    def __init__(self, game_model: GameModel) -> None:
        '''
        constructor
        game_model: (GameModel) model/data/state of the game
        '''
        self.game_model = game_model

    def handle_game_events(self, event):
        '''
        Handles game specific user input during the game
        '''
        if event.type != pygame.KEYDOWN:
            return

        if event.key in [pygame.K_a, pygame.K_LEFT]:
            self.game_model.move_character_left()
        elif event.key in [pygame.K_d, pygame.K_RIGHT]:
            self.game_model.move_character_right()
        elif event.key in [pygame.K_o, pygame.K_o]:
            self.game_model.is_over = True
