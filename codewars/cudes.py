# https://www.codewars.com/kata/playing-with-cubes-ii/train/python

class Cube:
    def __init__(self, whatever=0):
        self._side = abs(whatever)

    def get_side(self):
        """Return the side of the Cube"""
        return self._side

    def set_side(self, new_side):
        """Set the value of the Cube's side."""
        self._side = abs(new_side)


#  c = Cube()
# c._side = 4   # starts with _
                # warning do not touch from outside
