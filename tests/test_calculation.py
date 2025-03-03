"""
This module contains tests for the calculator operations and Calculation class.

The tests are designed to verify the correctness of basic arithmetic operations
(addition, subtraction, multiplication, division) implemented in the calculator.operations module,
as well as the functionality of the Calculation class that encapsulates these operations.
"""
from decimal import Decimal  # Standard library import comes first
import pytest
from app.operations.operations import add, divide
from app.calculation.calculation import Calculation

# Fixture to provide operand1
@pytest.fixture
def operand1():
    """Fixture to provide the first operand for calculations."""
    return Decimal('14')

# Fixture to provide operand2
@pytest.fixture
def operand2():
    """Fixture to provide the second operand for calculations."""
    return Decimal('7')

# Fixture to provide the operation (add)
@pytest.fixture
def operation():
    """Fixture to provide the arithmetic operation (addition)."""
    return add

# Fixture to provide expected result
@pytest.fixture
def expected():
    """Fixture to provide the expected result of the operation."""
    return Decimal('21')  # Adjust based on the operation you are testing

def test_calculation_operations(operand1, operand2, operation, expected):
    """Test calculation operations with various operands and expected results."""
    calc = Calculation(operand1, operand2, operation)
    assert calc.perform() == expected, f"Failed {operation.__name__} operation with {operand1} and {operand2}"

def test_calculation_repr():
    """Test the string representation (_repr_) of the Calculation class."""
    calc = Calculation(Decimal('14'), Decimal('7'), add)
    expected_repr = "Calculation(14, 7, add)"
    assert repr(calc) == expected_repr, "The _repr_ method output does not match the expected string."

def test_divide_by_zero():
    """Test division by zero to ensure it raises a ValueError."""
    calc = Calculation(Decimal('12'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.perform()
