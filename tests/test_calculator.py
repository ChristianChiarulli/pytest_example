import pytest

from calculator.calculator import Calculator


@pytest.fixture
def calculator():
    return Calculator()


def test_addition(calculator):
    assert calculator.add(1, 2) == 3
    assert calculator.add(-1, 1) == 0
    assert calculator.add(5, 7) == 12


def test_subtraction(calculator):
    assert calculator.subtract(5, 3) == 2
    assert calculator.subtract(0, 5) == -5
    assert calculator.subtract(3, 3) == 0


def test_multiplication(calculator):
    assert calculator.multiply(3, 4) == 12
    assert calculator.multiply(-2, 6) == -12
    assert calculator.multiply(5, 0) == 0


def test_division(calculator):
    assert calculator.divide(6, 2) == 3
    assert calculator.divide(9, 3) == 3
    assert calculator.divide(-12, 4) == -3


def test_division_by_zero(calculator):
    with pytest.raises(ValueError, match="Division by zero is not allowed"):
        calculator.divide(10, 0)
