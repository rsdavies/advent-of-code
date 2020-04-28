import pytest
from day_4 import meets_criteria


def test_meets_criteria():
    tests = [111111, 223450, 123789, 577889, 112233, 123444, 111122]
    expected = [False, False, False, True, True, False, True]

    actual = [meets_criteria(password) for password in tests]

    assert actual == expected
