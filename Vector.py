import math


class Vector:
    """
    A class that represents a 3D vector with x, y, and z components.
    """

    __slots__ = ["x", "y", "z"]

    def __init__(self, x: int | float, y: int | float, z: int | float):
        """
        Initializes a new Vector instance with the specified x, y, and z components.

        :param x: The x component of the vector.
        :param y: The y component of the vector.
        :param z: The z component of the vector.
        """

        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other: 'Vector'):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: 'Vector'):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __eq__(self, other: 'Vector'):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def get_magnitude(self) -> float:
        """
        Computes the magnitude (or length) of the vector.

        :return: The magnitude of the vector as a float.
        """

        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def dot(self, other: 'Vector') -> int | float:
        """
        Computes the dot product of this vector with another vector.

        :param other: The other vector to compute the dot product with.
        :return: The dot product of the two vectors as an int or float.
        """

        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other: 'Vector') -> 'Vector':
        """
        Computes the cross product of this vector with another vector.
        Performs `self cross other`.

        :param other: The other vector to compute the cross product with.
        :return: A new Vector representing the cross product of the two vectors.
        """

        return Vector(
            (self.y * other.z - self.z * other.y),
            -(self.x * other.z - self.z * other.x),
            (self.x * other.y - self.y * other.x)
        )

    def normalise(self) -> None:
        """
        Normalizes this vector by scaling it to a unit vector of length 1.
        If the vector has a magnitude of zero, this method does nothing.

        :return: None
        """

        magnitude = self.get_magnitude()

        if magnitude:
            self.x /= magnitude
            self.y /= magnitude
            self.z /= magnitude

    def reverse(self) -> None:
        """
        Reverses the direction of this vector, effectively scaling it by -1.

        :return: None
        """

        self.x = -self.x
        self.y = -self.y
        self.z = -self.z
