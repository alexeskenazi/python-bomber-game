from src.display import Display
from src.helper import Helper


class GameoverScreen:
    '''
    GameoverScreen displays the game over screen
    '''

    def __init__(self, display: Display) -> None:
        '''
        constructor
        display: (Display) object containing the display information.
        '''
        self.display = display

    def draw(self):
        '''
        Draws the screen.
        '''
        self.display_game_over()

    def display_game_over(self):
        '''
        Displays the Game Over Message on the screen.
        '''
        surface = self.display.surface
        x_text = self.display.width / 2
        y_text = self.display.height / 2

        text = 'Game Over'
        font_size = 100
        Helper.print(surface, text, font_size, (x_text, y_text))

        y_text += font_size
        text = 'Press SPACE to restart'
        font_size = 50
        Helper.print(surface, text, font_size, (x_text, y_text))

        y_text += font_size
        text = 'Press Q to quit'
        font_size = 30
        Helper.print(surface, text, font_size, (x_text, y_text))

        y_text += font_size
        text = 'Press S to toggle sound'
        font_size = 30
        Helper.print(surface, text, font_size, (x_text, y_text))
