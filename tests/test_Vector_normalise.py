import pytest
from Vector import Vector


def test_normalise_unit_vector():
    # Create a unit vector and normalise it
    v = Vector(1, 0, 0)
    v.normalise()

    # Check that the vector is still a unit vector
    assert v.get_magnitude() == pytest.approx(1.0)
    assert v == Vector(1, 0, 0)


def test_normalise_zero_vector():
    # Create a zero vector and normalise it
    v = Vector(0, 0, 0)
    v.normalise()

    # Check that the vector is still a zero vector
    assert v.get_magnitude() == pytest.approx(0.0)
    assert v == Vector(0, 0, 0)


def test_normalise_arbitrary_vector():
    # Create an arbitrary vector and normalise it
    v = Vector(1, 2, 3)
    v.normalise()

    # Check that the magnitude of the vector is 1
    assert v.get_magnitude() == pytest.approx(1.0)

    # Check that the direction of the vector is preserved
    assert v.x == pytest.approx(0.2673, abs=1e-4)
    assert v.y == pytest.approx(0.5345, abs=1e-4)
    assert v.z == pytest.approx(0.8018, abs=1e-4)
