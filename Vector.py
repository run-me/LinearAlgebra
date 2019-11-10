from math import sqrt


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

    def vector_sum(self, v):
        assert v.dimension == self.dimension, "Dimensions should be same to perform vector sum"
        vector_sum = [x + y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(vector_sum)

    def vector_diff(self, v):
        assert v.dimension == self.dimension, "Dimensions should be same to perform vector subtraction"
        vector_difference = [x - y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(vector_difference)

    def scale_vector(self, scale):
        vector_scaled = [scale * coordinates for coordinates in self.coordinates]
        return Vector(vector_scaled)

    def magnitude(self):
        coordinates_squared = [x**2 for x in self.coordinates]
        return sqrt(sum(coordinates_squared))

    def normalize(self):
        vec_mag = self.magnitude()
        unit_vector = [x / vec_mag for x in self.coordinates]
        return Vector(unit_vector)


v1 = Vector([5.581, -2.136])
print(v1.magnitude())
print(v1.normalize().coordinates)
v2 = Vector([1.996, 3.108, -4.554])
print(v2.magnitude())
print(v2.normalize().coordinates)
