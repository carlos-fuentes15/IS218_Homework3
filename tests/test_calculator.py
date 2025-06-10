import pytest  # type: ignore
from calculator.calculation import Calculation
from calculator.history import Calculations


def test_addition():
    calc = Calculation(3, 2, '+')
    Calculations.add_calculation(calc)
    assert Calculations.last().get_result() == 5

def test_divide_by_zero():
    calc = Calculation(10, 0, '/')
    with pytest.raises(ZeroDivisionError):
        calc.get_result()

def test_division_by_zero_branch():
    calc = Calculation(10, 0, '/')
    with pytest.raises(ZeroDivisionError):
        calc.get_result()

def test_invalid_operator():
    calc = Calculation(4, 2, '%')
    with pytest.raises(ValueError):
        calc.get_result()

def test_clear_history():
    Calculations.clear()
    assert not Calculations.history

def test_division():
    calc = Calculation(10, 2, '/')
    assert calc.get_result() == 5

def test_string_representation():
    calc = Calculation(4, 2, '+')
    assert str(calc) == "4+2=6"

def test_string_representation_add():
    calc = Calculation(4, 2, '+')
    result = str(calc)
    assert result == "4+2=6"

def test_string_representation_multiply():
    calc = Calculation(3, 3, '*')
    result = str(calc)
    assert result == "3*3=9"

def test_str_method_coverage():
    calc = Calculation(5, 5, '+')
    assert str(calc) == "5+5=10"

def test_subtraction_explicit():
    calc = Calculation(10, 3, '-')
    assert calc.get_result() == 7

def test_static_multiply():
    assert Calculation.multiply(3, 4) == 12

def test_calculation_count():
    Calculations.clear()
    Calculations.add_calculation(Calculation(1, 2, '+'))
    assert Calculations.count() == 1
