import pytest

from day_1 import calculate_fuel


def test_1():
    assert calculate_fuel(12) == 2


def test_2():
    assert calculate_fuel(14) == 2


def test_3():
    assert calculate_fuel(1969) == 966


def test_4():
    assert calculate_fuel(100756) == 50346

