import pygame


class Image:
    # constructor
    def __init__(self, image_name: str, width, height):
        '''
        constructor
        image_name: (str) file name for the character image
        height: (int) the height of the rectangle
        width: (int) the width of the rectangle
        '''
        self.image_name = image_name
        self.height = height
        self.width = width
        self.rect = pygame.Rect
        self.image = pygame.image.load(image_name)
        self.image = pygame.transform.scale(self.image,
                                            (self.width, self.height))

    def draw(self, surface, x, y):
        '''
        Displays image on the surface
        surface: (pygame surface) Surface to display image on.
        '''

        image_loc = self.image.get_rect()
        image_loc.left = x
        image_loc.top = y

        surface.blit(self.image, image_loc)
