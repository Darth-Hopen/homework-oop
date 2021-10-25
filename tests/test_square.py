"""Tests for Square"""
from source.Square import Square
import pytest

name = "Square"


def test_create_class():
    square = Square(name, 2)
    assert isinstance(square, Square)
    assert (square.a, square.name, square.angles) == (2, name, 4)


def test_square_perimeter():
    square = Square(name, a=10)
    assert square.perimeter() == 40


def test_square_area():
    square = Square(name, a=10)
    assert square.area() == 100


def test_add_areas():
    square1 = Square(name, 4)
    square2 = Square(name, 5)
    assert square1.add_area(square2) == 41


def test_add_areas_error():
    var = 0
    square = Square(name, a=10)
    with pytest.raises(AttributeError):
        square.add_area(var)
