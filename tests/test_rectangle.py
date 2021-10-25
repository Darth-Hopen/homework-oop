"""Tests for Rectangle"""
from source.Rectangle import Rectangle
import pytest

name = "Rectangle"


@pytest.mark.parametrize('a, b', [(10, 5),
                                  (5, 10),
                                  (10, 10)
                                  ])
def test_create_rectangle_with_valid_values(a, b):
    if a > b:
        rectangle = Rectangle(name, a, b)
        assert rectangle.name == name
    elif a < b:
        rectangle = Rectangle(name, a, b)
        assert rectangle.name == name
    elif a == b:
        with pytest.raises(ValueError):
            rectangle = Rectangle(name, a, b)


def test_create_class():
    rectangle = Rectangle(name, a=10, b=5)
    assert isinstance(rectangle, Rectangle)
    assert rectangle.angles == 4


def test_rectangle_perimeter():
    rectangle = Rectangle(name, a=10, b=5)
    assert rectangle.perimeter() == 30


def test_rectangle_area():
    rectangle = Rectangle(name, a=10, b=5)
    assert rectangle.area() == 50


def test_add_areas():
    rectangle = Rectangle(name, a=10, b=5)
    assert rectangle.add_area(rectangle) == 100


def test_add_areas_error():
    var = 10
    rectangle = Rectangle(name, a=10, b=5)
    with pytest.raises(AttributeError):
        rectangle.add_area(var)
