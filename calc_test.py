from simple_calc import *

def test_sum():
    operand1 = 3
    operand2 = 3
    sum_result = 6
    calculator = Calc()
    assert calculator.add(operand1, operand2) == sum_result

def test_diff():
    operand1 = 5
    operand2 = 3
    difference = 2
    calculator = Calc()
    assert calculator.subtract(operand1, operand2) == difference

def test_zero_add():
    operand1 = 0
    operand2 = 2
    sum_result = operand2
    calculator = Calc()
    assert calculator.add(operand1, operand2) == sum_result

def test_add_zero():
    operand1 = 5
    operand2 = 0
    sum_result = operand1
    calculator = Calc()
    assert calculator.add(operand1, operand2) == sum_result

def test_nine_add():
    operand1 = 9
    operand2 = 2
    sum_result = 11
    calculator = Calc()
    assert calculator.add(operand1, operand2) == sum_result

def test_add_nine():
    operand1 = 2
    operand2 = 9
    sum_result = 11
    calculator = Calc()
    assert calculator.add(operand1, operand2) == sum_result

def _test_ten_add():
    operand1 = 10
    operand2 = 4
    sum_result = 14
    calculator = Calc()
    assert calculator.add(operand1, operand2) == sum_result

def _test_add_ten():
    operand1 = 3
    operand2 = 10
    sum_result = 13
    calculator = Calc()
    assert calculator.add(operand1, operand2) == sum_result

def test_subtract_zero():
    operand1 = 3
    operand2 = 0
    difference = operand1
    calculator = Calc()
    assert calculator.subtract(operand1, operand2) == difference

def test_zero_subtract():
    operand1 = 0
    operand2 = 3
    difference = -operand2
    calculator = Calc()
    assert calculator.subtract(operand1, operand2) == difference

def test_nine_subtract():
    operand1 = 9
    operand2 = 3
    difference = 6
    calculator = Calc()
    assert calculator.subtract(operand1, operand2) == difference

def test_subtract_nine():
    operand1 = 3
    operand2 = 9
    difference = -6
    calculator = Calc()
    assert calculator.subtract(operand1, operand2) == difference

def _test_ten_subtract():
    operand1 = 10
    operand2 = 4
    sum_result = 6
    calculator = Calc()
    assert calculator.subtract(operand1, operand2) == sum_result

def _test_subtract_ten():
    operand1 = 3
    operand2 = 10
    sum_result = -7
    calculator = Calc()
    assert calculator.subtract(operand1, operand2) == sum_result

''' 
Test cases
    Normal addition
    Normal subtraction
    Lower edge add (0 and -1)
    Upper edge add (9 and 10)
    Lower edge subtract (0 and -1)
    Upper edge subtract (9 and 10)
'''