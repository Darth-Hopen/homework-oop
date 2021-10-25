"""Tests for Triangle"""
from source.Triangle import Triangle
import pytest


def test_create_triangle():
    triangle = Triangle(a=10, b=12, c=5)
    assert isinstance(triangle, Triangle)
    assert (triangle.a, triangle.b, triangle.c, triangle.name, triangle.angles) == (10, 12, 5, 'Triangle', 3)


def test_triangle_perimeter():
    triangle = Triangle(a=5, b=6, c=7)
    assert triangle.perimeter() == 18


def test_triangle_area():
    triangle = Triangle(a=7, b=7, c=5)
    assert triangle.area() == 9


def test_add_areas():
    triangle = Triangle(a=5, b=6, c=15)
    assert triangle.add_area(triangle) == 26


def test_add_areas_error():
    var = 10
    triangle = Triangle(a=5, b=6, c=15)
    with pytest.raises(AttributeError):
        triangle.add_area(var)
