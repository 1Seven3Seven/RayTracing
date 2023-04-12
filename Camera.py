import math

from Vector import Vector
from Rotation import Rotation


class Camera:
    def __init__(self, view_window: tuple[int, int]):
        # Position and direction
        self.position: Vector = Vector(0, 0, 0)
        self.rotation: Rotation = Rotation(0, 0)

        # Field of view
        # https://en.wikipedia.org/wiki/Field_of_view_in_video_games
        self.view_window: tuple[int, int] = view_window
        self._fov_x: float = 90.0
        self._fov_y: float = 2 * math.atan(math.tan(self._fov_x / 2) * self.view_window[1] / self.view_window[0])

    @property
    def fov_x(self) -> float:
        return self._fov_x

    @property
    def fov_y(self) -> float:
        return self._fov_y

    @fov_x.setter
    def fov_x(self, new_fov: float) -> None:
        self._fov_x = new_fov
        self._fov_y: float = 2 * math.atan(math.tan(self._fov_x / 2) * self.view_window[1] / self.view_window[0])
