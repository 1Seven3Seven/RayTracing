from dataclasses import dataclass


@dataclass
class Rotation:
    """
Represents a rotation of Vector(0, 0, 1) that is to be performed.
    """

    # Rotation to the left and right, around the vertical axis
    yaw: float
    # Rotation down and up, around the horizontal axis
    pitch: float
