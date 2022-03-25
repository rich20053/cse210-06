import constants
from game.casting.hazzard import Hazzard
from game.shared.point import Point


class Truck(Hazzard):
    """
    Try not to run into this item.
    
    The responsibility of Obstacle is to select a random position and set it up as another way for a cycle to lose a game.

    Attributes:
        None.
    """
    def __init__(self, x, y):
        super().__init__(length)
        self.set_text("T")
        self.set_color(constants.YELLOW)
        position = Point(x,y)
        newpos = position.scale(constants.CELL_SIZE)
        self.set_position(newpos)
        self._prepare_body(x,y)

        