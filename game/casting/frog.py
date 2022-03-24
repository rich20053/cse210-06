import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Frog(Actor):
    """
    This is the Frog that moves in the game and it is also an obstacle for another way to lose.
    """
    def __init__(self):
        super().__init__()
        # Set the text and color of the frog.
        self.set_text("#")
        self.set_color(constants.GREEN)
        # Create the position of the Frog.
        position = Point(int(constants.COLUMNS / 2), 14)
        newposition = position.scale(constants.CELL_SIZE)
        self.set_position(newposition)
        # Set the score, Frog not on log or turtle, and that the game is not over. 
        self.score = 0
        self._on_log_turtle = False
        self._is_game_over = False
        
    def set_game_over(self):
        # This will end the game when called. 
        self._is_game_over = True

    def move_next(self):
        """Moves the frog to its next position according to its velocity. Will wrap the position 
        from one side of the screen to the other when it reaches the given maximum x and y values.
        
        Args:
            None.
        """
        # If the game is over we don't want to move.
        if (self._is_game_over):
            return
        x = (self._position.get_x() + self._velocity.get_x())
        if (x > constants.MAX_X - 41):
            x = constants.MAX_X - 41
        if (x < 0):
            x = 0
        y = (self._position.get_y() + self._velocity.get_y()) 
        if (y > constants.MAX_Y - 41):
            y = constants.MAX_Y - 41
        if (y < 0):
            y = constants.MAX_Y - 41
            self.add_score(1)
        # Sets the new position.
        self._position = Point(x, y)

    def add_score(self, score):
        self._score += score

    def get_score(self):
        g_score = self._score
        self._score = 0
        return(g_score)
    
    def set_on_log_or_turtle(self):
        self._on_log_turtle = True
        
    def set_off_log_or_turtle(self):
        self._on_log_turtle = False
        
    def is_on_log_or_turtle(self):
        return(self._on_log_turtle)
    
    def set_velocity(self, velocity):
        """
        Updates the velocity.
        """
        self._velocity = velocity

    def set_velocity_and_move(self, velocity):
        """
        Updates the velocity and calls move_next.
        """
        old_velocity = self._velocity.get_y()
        self._velocity = velocity
        new_velocity = self._velocity.get_y()
        if (old_velocity != new_velocity):
            self.move_next()
        
