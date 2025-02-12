import pygame


class Helper:
    '''
    Helper class to display text on the screen.
    '''

    def print(surface, text: str, size: int, center):
        '''
        Displays centered text on the input coordinates.
        surface: (Surface) pygame surface to print on.
        text: (str) text to print
        size: (int) font size
        center: (Point) coordinates to display at
        '''
        font = pygame.font.Font('freesansbold.ttf', size)
        TextSurf = font.render(text, True, 'white')
        TextRect = TextSurf.get_rect()
        TextRect.center = center
        surface.blit(TextSurf, TextRect)
