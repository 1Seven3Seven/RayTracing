import math

from Plane import Plane
from Vector import Vector
from Rotation import Rotation


class Camera:
    """
    A class representing a camera in a 3D space.
    """

    def __init__(self, view_window: tuple[int, int]):
        """
        Initializes a new instance of the Camera class for the given view window.

        :param view_window: A tuple representing the dimensions of the screen to be rendered to (width, height).
        """

        # Position and rotation
        self.position: Vector = Vector(0, 0, 0)
        self.current_rotation: Rotation = Rotation(0, 0)

        # Vectors created to show direction after rotation to the standard forward vector (0, 0, 1)
        # These should always be unit vectors
        self.forward_vector = Vector(0, 0, 1)
        self.upward_vector = Vector(0, 1, 0)
        self.right_vector = Vector(1, 0, 0)

        # Field of view
        self.view_window: tuple[int, int] = view_window
        self.aspect = self.view_window[0] / self.view_window[1]
        self.inverse_aspect = self.view_window[1] / self.view_window[0]
        self._fov_x: float = 90.0
        self._fov_y: float = self.get_y_fov_from_x_fov(self._fov_x, self.inverse_aspect)

    @staticmethod
    def get_x_fov_from_y_fov(fov_y: int | float, aspect: int | float):
        """
        Calculates the horizontal field of view from the vertical field of view and aspect ratio.
        https://en.wikipedia.org/wiki/Field_of_view_in_video_games

        :param fov_y: The vertical field of view angle in radians.
        :param aspect: The aspect ratio of the view window (width / height).
        :return: The horizontal field of view angle in radians.
        """

        return 2 * math.atan(math.tan(fov_y / 2) * aspect)

    @staticmethod
    def get_y_fov_from_x_fov(fov_x: int | float, inverse_aspect: int | float):
        """
        Calculates the vertical field of view from the horizontal field of view and aspect ratio.
        https://en.wikipedia.org/wiki/Field_of_view_in_video_games

        :param fov_x: The horizontal field of view angle in radians.
        :param inverse_aspect: The inverse of the aspect ratio of the view window (height / width).
        :return: The vertical field of view angle in radians.
        """

        return 2 * math.atan(math.tan(fov_x / 2) * inverse_aspect)

    @property
    def fov_x(self) -> float:
        """
        The horizontal field of view angle in radians.

        :return: The current horizontal field of view angle.
        """

        return self._fov_x

    @property
    def fov_y(self) -> float:
        """
        The vertical field of view angle in radians.

        :return: The current vertical field of view angle.
        """

        return self._fov_y

    @fov_x.setter
    def fov_x(self, new_fov: float) -> None:
        """
        Sets the horizontal field of view for the camera.
        Adjusts the vertical field of view with regard to the view window aspect ratio.

        :param new_fov: The new horizontal field of view angle in radians.
        :return: None
        """

        self._fov_x = new_fov
        self._fov_y: float = self.get_y_fov_from_x_fov(self._fov_x, self.inverse_aspect)

    @fov_y.setter
    def fov_y(self, new_fov: float) -> None:
        """
        Sets the vertical field of view for the camera.
        Adjusts the horizontal field of view with regard to the view window aspect ratio.

        :param new_fov: The new vertical field of view angle in radians.
        :return: None
        """

        self._fov_y = new_fov
        self._fov_x: float = self.get_x_fov_from_y_fov(self._fov_y, self.aspect)

    def get_near_plane(self):
        """
        Calculates the near plane in the forward direction of the camera 1 unit from the position.

        :return: A Plane object representing the near plane in the forward direction of the camera.
        """

        return Plane(self.forward_vector, self.position + self.forward_vector)
