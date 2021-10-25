"""Tests for Circle"""
from source.Circle import Circle

import pytest


def test_create_circle():
    circle = Circle(radius=10)
    assert isinstance(circle, Circle)
    assert (circle.radius, circle.angles, circle.name) == (10, 0, 'Circle')


def test_circle_perimeter():
    circle = Circle(radius=10)
    assert circle.perimeter() == 62


def test_circle_area():
    circle = Circle(radius=10)
    assert circle.area() == 314


def test_add_areas():
    circle1 = Circle(3)
    circle2 = Circle(6)
    assert circle1.add_area(circle2) == 141


def test_add_areas_error():
    var = 10
    circle = Circle(radius=10)
    with pytest.raises(AttributeError):
        circle.add_area(var)
