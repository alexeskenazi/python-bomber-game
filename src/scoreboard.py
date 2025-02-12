from src.game_model import GameModel
from src.helper import Helper
from src.image import Image
from src.assets import Assets
from src.display import Display


class Scoreboard():
    '''
    View for the scoreboard
    '''

    def __init__(self, display: Display, game_model: GameModel) -> None:
        '''
        constructor
        display: (Display) object containing the display information.
        game_model: (GameModel) model/data/state of the game
        '''
        self.display = display
        self.game_model = game_model
        self.init_health_image()

    def init_health_image(self):
        '''
        Initialize the life image
        '''
        width = self.display.lane_width / 2
        height = self.display.lane_width / 2
        image_file = Assets.images.get('health')
        self.health_image = Image(image_file, width, height)

    def draw(self):
        '''
        Draws the scoreboard
        '''
        self.draw_health()
        self.draw_score()
        self.draw_max_score()

    def draw_health(self):
        '''
        Draws the health meter in the scoreboard
        '''
        health = self.game_model.character.lives
        margin = self.display.lane_width / 2
        for live in range(health):
            x_health = margin + margin * live
            y_health = margin / 2
            self.health_image.draw(self.display.surface, x_health, y_health)

    def draw_score(self):
        '''
        Draws the score in the scoreboard
        '''
        score = self.game_model.get_score()
        font_size = 30
        margin = self.display.lane_width / 2
        x_score = self.display.width / 2
        y_text = margin
        text_score = 'Score: ' + str(score)
        Helper.print(self.display.surface, text_score, font_size,
                     (x_score, y_text))

        speed = self.game_model.game_speed_factor
        text_speed = 'speed: ' + str(speed)
        y_text += font_size
        font_size = 25
        Helper.print(self.display.surface, text_speed, font_size,
                     (x_score, y_text))

    def draw_max_score(self):
        '''
        Draws the max score in the scoreboard
        '''
        max_score = self.game_model.max_score
        margin = self.display.lane_width / 2
        x_score = self.display.width - 3 * margin
        y_score = margin
        text_score = 'Max: ' + str(max_score)
        Helper.print(self.display.surface, text_score, 30, (x_score, y_score))
