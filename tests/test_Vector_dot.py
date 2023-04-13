import math
import pytest

from Vector import Vector


@pytest.fixture
def vector():
    return Vector(1, 2, 3)


@pytest.fixture
def orthogonal_vector():
    return Vector(1, -2, 1)


def test_dot_product(vector):
    vector2 = Vector(4, 5, 6)
    dot_product = vector.dot(vector2)
    assert dot_product == pytest.approx(32)


def test_dot_product_same_vector(vector):
    dot_product = vector.dot(vector)
    assert dot_product == pytest.approx(14)


def test_dot_product_zero_vector(vector):
    zero_vector = Vector(0, 0, 0)
    dot_product = vector.dot(zero_vector)
    assert dot_product == pytest.approx(0)


def test_dot_product_negative_vector(vector):
    negative_vector = Vector(-1, -2, -3)
    dot_product = vector.dot(negative_vector)
    assert dot_product == pytest.approx(-14)


def test_dot_product_orthogonal_vectors(vector, orthogonal_vector):
    dot_product = vector.dot(orthogonal_vector)
    assert dot_product == pytest.approx(0)
