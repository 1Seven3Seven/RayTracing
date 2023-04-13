from Vector import Vector


class Plane:
    """
    Represents a plane in three-dimensional space.

    A plane is defined by a normal vector and a point on the plane.
    """

    def __init__(self, normal: Vector, point: Vector):
        self.normal: Vector = normal
        self.point: Vector = point

        self.constant: int | float = normal.x * point.x + normal.y * point.y + normal.z * point.z

    def __eq__(self, other: 'Plane'):
        """
        Checks if this plane is equal to another plane.

        :param other: The other plane to compare to this plane.
        :return: True if the two planes are equal, False otherwise.
        """

        return self.normal == other.normal and self.constant == other.constant

    def __str__(self):
        """
        Returns a string representation of this plane.

        :return: A string representation of this vector in the format "ax + by + cz = d".
        """

        return f"{self.normal.x}x + {self.normal.y}y + {self.normal.z} + z = {self.constant}"

    def __repr__(self):
        """
        Returns a string representation of this plane that can be used to recreate it.

        :return: A string representation of this plane in the format "Plane(Vector(a, b, c), Vector(x, y, z))" where
        a, b, c are the components of the normal vector and x, y, z is a point on the plane.
        """

        return f"Plane({self.normal.__repr__()}, {self.point.__repr__()})"
