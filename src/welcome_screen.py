from src.display import Display
from src.helper import Helper
from src.assets import Assets
from src.image import Image


class WelcomeScreen:
    '''
    WelcomeScreen is the view for the apps welcome screen.
    '''

    def __init__(self, display: Display) -> None:
        '''
        constructor
        display: (Display) object containing the display information.
        '''
        self.display = display
        self.init_welcome_charater_image()

    def init_welcome_charater_image(self):
        '''
        Intializes the main character large image
        '''
        image_file = Assets.images.get('welcome-character')
        image_width = self.display.width / 4
        image_height = self.display.height / 4
        self.welcome_image = Image(image_file, image_width, image_height)

    def draw(self):
        '''
        Draws the welcome screen.
        '''
        self.draw_game_title()
        self.draw_welcome_character()
        self.display_instructions()

    def draw_game_title(self):
        '''
        Draws the app title
        '''
        surface = self.display.surface
        x_text = self.display.width / 2
        y_text = self.display.height / 2

        text = 'Mario Bomber'
        font_size = 100
        Helper.print(surface, text, font_size, (x_text, y_text))

        y_text += font_size
        text = 'Press SPACE to start'
        font_size = 50
        Helper.print(surface, text, font_size, (x_text, y_text))

        y_text += 2 * font_size
        text = 'By Alex E. and Vishil P.'
        font_size = 30
        Helper.print(surface, text, font_size, (x_text, y_text))

    def display_instructions(self):
        '''
        Prints the game instructions on the screen.
        '''
        surface = self.display.surface
        x_text = self.display.width / 2
        y_text = self.display.height - 140

        text = 'Instructions: Bombs kill you :()'
        font_size = 20
        Helper.print(surface, text, font_size, (x_text, y_text))

        y_text += font_size
        text = 'Mushrooms keep you alive and give you a rush!'
        font_size = 20
        Helper.print(surface, text, font_size, (x_text, y_text))

        y_text += font_size
        text = 'Every evaded bomb gives you points'
        font_size = 20
        Helper.print(surface, text, font_size, (x_text, y_text))

        y_text += font_size
        text = 'S to control music'
        font_size = 20
        Helper.print(surface, text, font_size, (x_text, y_text))

        y_text += font_size
        text = 'R to reset the max score'
        font_size = 20
        Helper.print(surface, text, font_size, (x_text, y_text))

        y_text += font_size
        text = 'Q to Quit'
        font_size = 20
        Helper.print(surface, text, font_size, (x_text, y_text))

    def draw_welcome_character(self):
        '''
        Draws the main character in the screen.
        '''
        surface = self.display.surface
        x_image = self.display.width / 4
        y_image = self.display.height / 4
        self.welcome_image.draw(surface, x_image, y_image)
