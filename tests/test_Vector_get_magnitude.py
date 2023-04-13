import pytest

from Vector import Vector


@pytest.fixture
def vector():
    return Vector(1, 2, 3)


def test_get_magnitude(vector):
    assert vector.get_magnitude() == pytest.approx(3.7416573867739413)


def test_get_magnitude_zero():
    vector = Vector(0, 0, 0)
    assert vector.get_magnitude() == pytest.approx(0.0)


def test_get_magnitude_negative(vector):
    vector.x = -1
    vector.y = -2
    vector.z = -3
    assert vector.get_magnitude() == pytest.approx(3.7416573867739413)
