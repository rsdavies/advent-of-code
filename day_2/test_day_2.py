import pytest

from day_2 import Computer


def test_1():
    c = Computer([1, 0, 0, 0, 99])
    c.run()
    assert c.program == [2, 0, 0, 0, 99]


def test_2():
    c = Computer([2, 3, 0, 3, 99])
    c.run()
    assert c.program == [2, 3, 0, 6, 99]


def test_3():
    c = Computer([2, 4, 4, 5, 99, 0])
    c.run()
    assert c.program == [2, 4, 4, 5, 99, 9801]


def test_4():
    c = Computer([1, 1, 1, 4, 99, 5, 6, 0, 99])
    c.run()
    assert c.program == [30, 1, 1, 4, 2, 5, 6, 0, 99]

