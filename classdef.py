# Here all the Classes will be defined that are used in the game

class Player(object):
    # class def for the player
    def __init__(self, x, y, radius, col=(0, 0, 0)):
        self.points = 0
        self.x = x
        self.y = y
        self.radius = radius
        self.col = col  # default color is black

    def pos(self):
        # return the position of the player
        return (self.x, self.y)
