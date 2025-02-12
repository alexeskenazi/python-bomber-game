import os
import pygame


class Display:
    '''
    Wraps some pygame and display related information that is needed in different parts of the application.
    '''

    def __init__(self,
                 width: int = 1200,
                 height: int = 1000,
                 num_of_lanes: int = 10) -> None:
        '''
        constructor
        width: (int) application display width in pixels.
        width: (int) application display height in pixels.
        num_of_lanes: (int) number of lanes in the game. Used to calculate object sizes and positions.
        '''
        self.width = width
        self.height = height
        self.num_of_lanes = num_of_lanes
        self.lane_width = self.width / self.num_of_lanes

        self.fix_missing_display_error()
        self.setup_display_surface()

    def fix_missing_display_error(self):
        '''
        Fixes the 'missing display' pygame error that sometmes appear in Replit
        '''
        x = 100
        y = 0
        os.environ['SDL_VIDEO_WINDOW_POS'] = '%d,%d' % (x, y)

    def setup_display_surface(self):
        '''
        Sets up the applicaton background.
        '''
        self.surface = pygame.display.set_mode((self.width, self.height))
