from src.sound import Sound
from src.falling_object import FallingObject
from src.scoreboard import Scoreboard
from src.image import Image
from src.display import Display
from src.helper import Helper
from src.game_model import GameModel
from src.assets import Assets


class GameScreen:
    '''
    GameScreen is the view object for the game.
    '''

    def __init__(self, display: Display, game_model: GameModel) -> None:
        '''
        constructor
        display: (Display) object containing the display information.
        game_model: (GameModel) model/data/state of the game
        '''
        self.helper = Helper()
        self.display = display
        self.game_model = game_model
        self.scoreboard = Scoreboard(display, game_model)
        self.init_character_image()
        self.init_obj_image()
        self.init_life_image()
        self.init_win_sound()
        self.init_hit_sound()

    def draw(self):
        '''
        Draws the game view.
        '''
        self.draw_scoreboard()
        self.draw_character()
        self.draw_falling_objects()

    def init_character_image(self):
        '''
        Initializes the character image
        '''
        width = self.display.lane_width
        height = self.display.lane_width
        image_file = Assets.images.get('character')
        self.character_image = Image(image_file, width, height)

    def init_obj_image(self):
        '''
        Initializes the bomb image
        '''
        width = self.display.lane_width
        height = self.display.lane_width
        image_file = Assets.images.get('bomb')
        self.bomb_image = Image(image_file, width, height)

    def init_life_image(self):
        '''
        Initializes the life objects image
        '''
        width = self.display.lane_width
        height = self.display.lane_width
        image_file = Assets.images.get('life')
        self.life_image = Image(image_file, width, height)

    def init_win_sound(self):
        '''
        Initializes the win sound
        '''
        self.win_sound = Sound(Assets.sounds.get('win_sound'))

    def init_hit_sound(self):
        '''
        Initializes the win sound
        '''
        self.hit_sound = Sound(Assets.sounds.get('hit_sound'))

    def draw_character(self):
        '''
        Draws the character on the screen.
        '''
        x_character = self.display.lane_width * self.game_model.character.lane
        y_character = self.display.height * (
            100 - self.game_model.character.height) / 100
        self.character_image.draw(self.display.surface, x_character,
                                  y_character)

    def draw_falling_objects(self):
        '''
        Draws all the falling objects on the screen.
        '''
        for obj in self.game_model.falling_objects:
            self.draw_falling_object(obj)

    def draw_falling_object(self, obj: FallingObject):
        '''
        Draws a bomb on the screen.
        obj: (FallingObject) bomb to draw.
        '''
        if obj.is_state_active():
            self.draw_object_unexploted(obj)
            return

        if obj.is_state_evaded():
            self.draw_object_value(obj)
            return

        if obj.is_state_target_hit():
            self.draw_object_exploded(obj)
            return

    def draw_object_unexploted(self, obj: FallingObject):
        '''
        Draws a bomb in an unexploted state.
        obj: (FallingObject) bomb to draw.
        '''
        surface = self.display.surface
        x_obj, y_obj = self.get_obj_screen_pos(obj)
        if obj.type == 'bomb':
            self.bomb_image.draw(surface, x_obj, y_obj)
        elif obj.type == 'life':
            self.life_image.draw(surface, x_obj, y_obj)

    def draw_object_value(self, obj: FallingObject):
        '''
        Draws the bomb in exploded state. We currently display the score value of the item.
        obj: (FallingObject) bomb to draw.
        '''
        surface = self.display.surface
        x_obj, y_obj = self.get_obj_screen_pos(obj)
        x_text = x_obj + self.display.lane_width / 2
        y_text = y_obj
        text = str(obj.score_value)
        font_size = 40
        Helper.print(surface, text, font_size, (x_text, y_text))

    def draw_object_exploded(self, obj: FallingObject):
        '''
        Draws the bomb in exploded state. We currently display the score value of the item.
        obj: (FallingObject) bomb to draw.
        '''
        surface = self.display.surface
        x_obj, y_obj = self.get_obj_screen_pos(obj)
        x_text = x_obj + self.display.lane_width / 2
        y_text = y_obj
        if obj.is_bomb():
            text = 'BOOM!'
            font_size = 40
            if obj.is_just_hit():
                obj.reset_just_hit()
                self.hit_sound.beep()
            Helper.print(surface, text, font_size, (x_text, y_text))

        if obj.is_life():
            text = 'Life!'
            font_size = 40
            if obj.is_just_hit():
                obj.reset_just_hit()
                self.win_sound.beep()
            Helper.print(surface, text, font_size,
                         (self.display.width / 2, self.display.height / 2))

    def get_obj_screen_pos(self, obj: FallingObject):
        '''
        Calculates the screen position of the object by translating the logical units to pixels.
        obj: (FallingObject) bomb to draw.
        return: (tuple) Bomb coordinates in pixels
        '''
        x_obj = obj.lane * self.display.lane_width
        y_obj = obj.log_depth * self.display.height / 100
        return x_obj, y_obj

    def draw_scoreboard(self):
        '''
        Draws the scoreboard
        '''
        self.scoreboard.draw()
