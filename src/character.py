class MainCharacter():
    '''
    Screen object representing the main game character.
    '''

    def __init__(self, num_of_lanes: int) -> None:
        '''
        constructor
        num_of_lanes: (int) number of lanes in the game. Used to position the character in the logical gameboard.
        '''
        self.image = 'character'
        self.num_of_lanes = num_of_lanes
        self.lane = num_of_lanes / 2
        self.height = 15  # relative out of 100
        full_height = 100  # logical coords
        self.top = full_height - self.height
        self.visible = True
        self.lives = 3

    def add_life(self):
        '''
        Increases the number of lives by one.
        '''
        self.lives += 1

    def loose_life(self):
        '''
        Decreases the number of lives by one.
        '''
        self.lives -= 1

    def is_dead(self) -> bool:
        '''
        Checks if the character is still alive
        return: (bool) True if it is still alive
        '''
        return self.lives <= 0

    def move_right(self):
        '''
        Moves the character lane by one to the right.
        '''
        self.lane = (self.lane + 1) % self.num_of_lanes

    def move_left(self):
        '''
        Moves the character lane by one to the left.
        '''
        self.lane = (self.lane - 1) % self.num_of_lanes
