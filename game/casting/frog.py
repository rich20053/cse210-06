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
      
    def move_next(self):
        """Moves the frog to its next position according to its velocity. Will wrap the position 
        from one side of the screen to the other when it reaches the given maximum x and y values.
        Keeps the frog from going off the side.
        Args:
            None.
        """
        # If the game is over we don't want to move.
        x = (self._position.get_x() + self._velocity.get_x())
        y = (self._position.get_y() + self._velocity.get_y()) 
        self._position = Point(x, y)
  
    def set_velocity(self, velocity):
        """
        Updates the velocity.
        """
        self._velocity = velocity

        
