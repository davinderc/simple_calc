from simple_calc import *

def test_sum():
    addend1 = 3
    addend2 = 3
    sum = 6
    calculator = Calc()
    assert calculator.add(addend1, addend2) == sum

def test_diff():
    operand1 = 5
    operand2 = 3
    difference = 2
    calculator = Calc()
    assert calculator.subtract(operand1, operand2) == difference