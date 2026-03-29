"""
tests_1b.py

This module contains unit tests for the simple_calculator function defined in lab_1b.py.
"""

import pytest
from labs.lab_1.lab_1b import simple_calculator

def test_addition():
    assert simple_calculator("add", 5, 3) == 8          # Test for positive numbers
    assert simple_calculator("add", -2, 2) == 0         # Test for negative and positive number
    assert simple_calculator("add", 0, 0) == 0          # Test for zero addition
    assert simple_calculator("add", 0.00001, 0.25) == 0.25001 # Test for addition of decimals 
    assert simple_calculator("add", 6.022e23, 2.62e17) == pytest.approx(6.02200262e23) # Test for addition of large values in scientific notation

def test_subtraction():
    assert simple_calculator("subtract", 5, 3) == 2     # Test for positive numbers
    assert simple_calculator("subtract", -2, -2) == 0   # Test for negative numbers
    assert simple_calculator("subtract", 0, 5) == -5    # Test for zero minuend
    assert simple_calculator("subtract", 0.2, 0.01) == 0.19 # Test for subtracting decimals
    assert simple_calculator("subtract", 13.5, -2) == 15.5 # Test for subtracting a negative number from a positive number (adding by subtraction)
    assert simple_calculator("subtract", 6.022e23, 2.62e17) == pytest.approx(6.02199738e23) # Test for subtracting numbers in scientific notation

def test_multiplication():
    assert simple_calculator("multiply", 5, 3) == 15    # Test for positive numbers
    assert simple_calculator("multiply", -2, 2) == -4   # Test for negative and positive number
    assert simple_calculator("multiply", 0, 100) == 0   # Test for multiplication by zero
    assert simple_calculator("multiply", -200, -300) == 60000  # Test for multiplication of two negative numbers
    assert simple_calculator("multiply", 6.62e-34, 9.1e-31) == pytest.approx(6.0242e-64) # Test for multiplication of two extremely small numbers in scientific notation

def test_division():
    assert simple_calculator("divide", 6, 3) == 2       # Test for positive numbers
    assert simple_calculator("divide", -4, 2) == -2     # Test for negative and positive number
    assert simple_calculator("divide", 5, 2) == 2.5     # Test for division resulting in float

def test_division_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        simple_calculator("divide", 5, 0)               # Test division by zero

def test_invalid_operation():
    with pytest.raises(ValueError, match="Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'."):
        simple_calculator("modulus", 5, 3)              # Test for invalid operation
    with pytest.raises(ValueError, match="Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'."):
        simple_calculator("", 5, 3)                     # Test for empty operation

if __name__ == "__main__":
    pytest.main()