import pytest
from Vector import Vector


@pytest.fixture
def vector():
    return Vector(1, 2, 3)


def test_reverse_positive_vector(vector):
    # Test reversing a vector with positive components
    vector.reverse()
    assert vector == Vector(-1, -2, -3)


def test_reverse_negative_vector():
    # Test reversing a vector with negative components
    vector = Vector(-4, -5, -6)
    vector.reverse()
    assert vector == Vector(4, 5, 6)


def test_reverse_mixed_sign_vector():
    vector = Vector(-7, 8, -9)
    vector.reverse()
    assert vector == Vector(7, -8, 9)


def test_reverse_zero_vector():
    # Test reversing a vector with zero components
    vector = Vector(0, 0, 0)
    vector.reverse()
    assert vector == Vector(0, 0, 0)


def test_reverse_vector_twice(vector):
    # Test reversing a vector twice
    vector = Vector(2, 3, 4)
    vector.reverse()
    vector.reverse()
    assert vector == Vector(2, 3, 4)
