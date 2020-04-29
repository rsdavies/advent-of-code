import pytest
import mock
from day_5 import Computer


@pytest.mark.parametrize("test_input,expected",
                         [("-1", "-1\n"), ("10", "10\n")])
def test_day_5(monkeypatch, capsys, test_input, expected):
    program = [3, 0, 4, 0, 99]
    # need to mock up input?
    monkeypatch.setattr('builtins.input', lambda x: test_input)
    c = Computer(program)
    c.run()
    captured = capsys.readouterr()

    assert captured.out == expected


def test_parameter_mode():
    program = [1002, 4, 3, 4, 33]
    c = Computer(program)
    c.run()
    expected = [1002, 4, 3, 4, 99]
    assert c.program == expected


@pytest.mark.parametrize("test_input,expected",
                         [("8", "1\n"), ("10", "0\n")])
def test_1(monkeypatch, capsys, test_input, expected):
    program = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
    monkeypatch.setattr('builtins.input', lambda x: test_input)
    c = Computer(program)
    c.run()
    captured = capsys.readouterr()
    assert captured.out == expected


@pytest.mark.parametrize("test_input,expected",
                         [("8", "0\n"), ("10", "0\n"), ("2", "1\n")])
def test_2(monkeypatch, capsys, test_input, expected):
    program = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
    monkeypatch.setattr('builtins.input', lambda x: test_input)
    c = Computer(program)
    c.run()
    captured = capsys.readouterr()
    assert captured.out == expected


@pytest.mark.parametrize("test_input,expected",
                         [("8", "1\n"), ("10", "0\n"), ("2", "0\n")])
def test_3(monkeypatch, capsys, test_input, expected):
    program = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
    monkeypatch.setattr('builtins.input', lambda x: test_input)
    c = Computer(program)
    c.run()
    captured = capsys.readouterr()
    assert captured.out == expected


@pytest.mark.parametrize("test_input,expected",
                         [("8", "0\n"), ("10", "0\n"), ("2", "1\n")])
def test_4(monkeypatch, capsys, test_input, expected):
    program = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
    monkeypatch.setattr('builtins.input', lambda x: test_input)
    c = Computer(program)
    c.run()
    captured = capsys.readouterr()
    assert captured.out == expected


@pytest.mark.parametrize("test_input,expected",
                         [("0", "0\n"), ("10", "1\n"), ("-2", "1\n")])
def test_5(monkeypatch, capsys, test_input, expected):
    program = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
    monkeypatch.setattr('builtins.input', lambda x: test_input)
    c = Computer(program)
    c.run()
    captured = capsys.readouterr()
    assert captured.out == expected


@pytest.mark.parametrize("test_input,expected",
                         [("0", "0\n"), ("10", "1\n"), ("-2", "1\n")])
def test_6(monkeypatch, capsys, test_input, expected):
    program = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]
    monkeypatch.setattr('builtins.input', lambda x: test_input)
    c = Computer(program)
    c.run()
    captured = capsys.readouterr()
    assert captured.out == expected


@pytest.mark.parametrize("test_input,expected",
                         [("5", "999\n"), ("8", "1000\n"), ("100", "1001\n")])
def test_7(monkeypatch, capsys, test_input, expected):
    program = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20,
               1006, 20, 31, 1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
               999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]
    monkeypatch.setattr('builtins.input', lambda x: test_input)
    c = Computer(program)
    c.run()
    captured = capsys.readouterr()
    assert captured.out == expected