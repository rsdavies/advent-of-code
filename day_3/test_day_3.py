import pytest
from day_3 import distance, steps


def test_1():
    wire1 = ['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72']
    wire2 = ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']
    wires = [wire1, wire2]

    assert distance(wires) == 159


def test_2():
    wire1 = ['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51']
    wire2 = ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7']
    wires = [wire1, wire2]

    assert distance(wires) == 135


def test_3():
    wire1 = ['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72']
    wire2 = ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']
    wires = [wire1, wire2]

    assert steps(wires) == 610


def test_4():
    wire1 = ['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51']
    wire2 = ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7']
    wires = [wire1, wire2]

    assert steps(wires) == 410