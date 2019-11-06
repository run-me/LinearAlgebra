class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)
        except ValueError:
            raise ValueError("Specify coordinates to operate on")
        except TypeError:
            raise TypeError("The coordinates must be iterable")

    def __str__(self):
        return "Vector: {}".format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates
