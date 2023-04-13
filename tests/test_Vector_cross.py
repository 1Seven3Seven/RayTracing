import pytest

from Vector import Vector


@pytest.fixture
def vector():
    return Vector(1, 2, 3)


@pytest.fixture
def orthogonal_vector():
    return Vector(1, -2, 1)


@pytest.fixture
def standard_vector_x():
    return Vector(1, 0, 0)


@pytest.fixture
def standard_vector_y():
    return Vector(0, 1, 0)


def test_cross_standard_vectors(standard_vector_x, standard_vector_y):
    result = standard_vector_x.cross(standard_vector_y)
    assert result == Vector(0, 0, 1)


def test_cross_same_vector(vector):
    result = vector.cross(vector)
    assert result == Vector(0, 0, 0)


def test_cross_orthogonal_vectors(vector, orthogonal_vector):
    result = vector.cross(orthogonal_vector)
    assert result == Vector(8, 2, -4)
