import random


class FallingObject:
    '''
    Screen object representing a falling object that affects the character lives, game score, game speed, etc.
    '''
    num_of_lanes = 0

    def __init__(self,
                 type: str = 'bomb',
                 lane: int = 0,
                 use_random_lane: bool = False) -> None:
        '''
        constructor
        type: (str) Falling object type. Available types are 'bomb' and 'life'
        lane: (int) vertical lane where the falling object moves down.
        use_random_lane: (bool) whether to use hte lane input or use a random lane number
        '''
        self.type = type
        self.lane = lane
        self.use_random_lane = use_random_lane
        self.log_depth = 0  # depth as percent of the game vertical area.
        self.calc_object_height = self.calc_object_height()
        self.speed = 0
        self.set_state_active()
        self.score_value = 0
        self.just_hit = False  # True right after it hits target, reset to False on next update
        self.reset()

    def reset(self):
        '''
        Restores the falling object data.
        '''
        self.log_depth = 0
        self.if_needed_set_random_lane()
        self.set_random_speed()
        self.set_score_value()
        self.set_state_active()

    def if_needed_set_random_lane(self):
        '''
        Sets the lane randomly if the use_random_lane is set
        '''
        if self.use_random_lane:
            self.lane = self.get_random_lane()

    def get_image_name(self) -> str:
        '''
        return: (str) the image name
        '''
        return self.image

    def drop(self, speed_factor: float = 1):
        '''
        Updates the position of the falling object vertically according to the speed
        speed_factor: (float) Factor used to multiply the speed of the falling object
        '''
        full_height = 100
        new_height = self.log_depth + self.speed * speed_factor
        if new_height >= full_height:
            self.reset()
        self.log_depth = new_height % full_height

    def bottom(self) -> float:
        '''
        Returns the logical vertical coordinate of the bottom of the falling object
        return: (float) logical vertical coordinates
        '''
        return self.log_depth + self.calc_object_height

    def set_state_active(self):
        '''
        Sets the bomb state to active. 
        This is the state while the bomb is falling
        '''
        self.state = 'active'

    def set_state_evaded(self):
        '''
        Sets the bomb state to evaded.
        This is the state for a bomb that reached the bottom without hiting the character
        '''
        self.state = 'evaded'

    def set_state_target_hit(self):
        '''
        Sets the bomb state to target-hit.
        This is the state for a bomb that hit the character
        '''
        self.state = 'target_hit'
        self.just_hit = True

    def is_state_active(self) -> bool:
        '''
        return: (bool) True if the bomb state is active.
        '''
        return self.state == 'active'

    def is_state_evaded(self) -> bool:
        '''
        return: (bool) True if the bomb state is evaded.
        '''
        return self.state == 'evaded'

    def is_state_target_hit(self) -> bool:
        '''
        return: (bool) True if the bomb state is target_hit.
        '''
        return self.state == 'target_hit'

    def is_bomb(self) -> bool:
        '''
        return: (bool) True if the object type is a bomb
        '''
        return self.type == 'bomb'

    def is_life(self) -> bool:
        '''
        return: (bool) True if the object type is a life
        '''
        return self.type == 'life'

    def reset_just_hit(self):
        '''
        Sets the just hit to False
        '''
        self.just_hit = False

    def is_just_hit(self) -> bool:
        '''
        return: (bool) True if the object just hit the target
        '''
        return self.just_hit

    def get_random_lane(self) -> int:
        '''
        return: (int) random number between 0 and the number of game lanes.
        '''
        return random.randint(0, FallingObject.num_of_lanes - 1)

    def set_random_speed(self):
        '''
        Sets the object falling speed (randomly).
        '''
        min_speed = 5
        max_speed = 15
        falling_speed = random.randint(min_speed, max_speed) / 100
        self.speed = falling_speed

    def set_score_value(self, speed: float = 0):
        '''
        Converts the speed into a score value for the object
        '''
        full_height = 100
        factor = 4
        score_value = int(self.speed * factor * full_height)
        self.score_value = score_value

    def calc_object_height(self) -> float:
        '''
        calculates the object height in logical units
        '''
        full_height = 100
        return full_height / self.num_of_lanes
