from src.sound import Sound
from src.display import Display
from src.assets import Assets
from src.image import Image


class Background:
    '''
    Displays and manages the background image and sound
    '''

    def __init__(self, display: Display) -> None:
        '''
        constructor
        display: (Display) object containing the display information.
        '''
        self.display = display
        self.init_background_image()
        self.init_background_sound()
        self.sound_on = False

    def init_background_image(self):
        '''
        Initializes the applicaton background.
        '''
        file_name = Assets.images.get('background')
        width = self.display.width
        height = self.display.height

        self.background_image = Image(file_name, width, height)

    def init_background_sound(self):
        '''
        Initializes the win sound
        '''
        self.background_sound = Sound(Assets.sounds.get('backgroun_sound'))

    def draw(self):
        '''
        Draws the application background
        '''
        self.background_image.draw(self.display.surface, 0, 0)

    def play_sound(self):
        '''
        Plays the bacground sound.
        '''
        self.sound_on = True
        self.background_sound.play()

    def stop_sound(self):
        '''
        Stops the bacground sound.
        '''
        self.sound_on = False
        self.background_sound.stop()

    def toggle_sound(self):
        '''
        Stops the bacground sound.
        '''
        if self.sound_on:
            self.stop_sound()
        else:
            self.play_sound()
