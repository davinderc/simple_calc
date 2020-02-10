from simple_calc import *
from contracts import ContractNotRespected
import pytest

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

def test_ten_add():
    operand1 = 10
    operand2 = 4
    sum_result = 14
    calculator = Calc()
    with pytest.raises(ContractNotRespected) as e:
        assert calculator.add(operand1, operand2) == sum_result
    assert "Breach for argument 'operand1'" in str(e.value)

def test_add_ten():
    operand1 = 3
    operand2 = 10
    sum_result = 13
    calculator = Calc()
    with pytest.raises(ContractNotRespected) as e:
        assert calculator.add(operand1, operand2) == sum_result
    assert "Breach for argument 'operand2'" in str(e.value)

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

def test_neg_one_subtract():
    operand1 = -1
    operand2 = 4
    difference = -5
    calculator = Calc()
    with pytest.raises(ContractNotRespected) as e:
        assert calculator.subtract(operand1, operand2) == difference
    assert "Breach for argument 'operand1'" in str(e.value)

def test_subtract_neg_one():
    operand1 = 9
    operand2 = -1
    difference = 10
    calculator = Calc()
    with pytest.raises(ContractNotRespected) as e:
        assert calculator.subtract(operand1, operand2) == difference
    assert "Breach for argument 'operand2'" in str(e.value)

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

def test_ten_subtract():
    operand1 = 10
    operand2 = 4
    difference = 6
    calculator = Calc()
    with pytest.raises(ContractNotRespected) as e:
        assert calculator.subtract(operand1, operand2) == difference
    assert "Breach for argument 'operand1'" in str(e.value)

def test_subtract_ten():
    operand1 = 3
    operand2 = 10
    difference = -7
    calculator = Calc()
    with pytest.raises(ContractNotRespected) as e:
        assert calculator.subtract(operand1, operand2) == difference
    assert "Breach for argument 'operand2'" in str(e.value)

def test_lower_corner_add():
    operand1 = -1
    operand2 = -1
    sum_result = -2
    calculator = Calc()
    with pytest.raises(ContractNotRespected) as e:
        assert calculator.add(operand1, operand2) == sum_result
    assert "Breach for argument 'operand1'" in str(e.value)

def test_lower_corner_subtract():
    operand1 = -1
    operand2 = -1
    difference = 0
    calculator = Calc()
    with pytest.raises(ContractNotRespected) as e:
        assert calculator.subtract(operand1, operand2) == difference
    print(e.value)
    assert "Breach for argument 'operand1'" in str(e.value)

def test_upper_corner_add():
    operand1 = 10
    operand2 = 10
    sum_result = 20
    calculator = Calc()
    with pytest.raises(ContractNotRespected) as e:
        assert calculator.add(operand1, operand2) == sum_result
    print(e.value)
    assert "Breach for argument 'operand1'" in str(e.value)

def test_upper_corner_subtract():
    operand1 = 10
    operand2 = 10
    difference = 0
    calculator = Calc()
    with pytest.raises(ContractNotRespected) as e:
        assert calculator.subtract(operand1, operand2) == difference
    print(e.value)
    assert "Breach for argument 'operand1'" in str(e.value)


test_lower_corner_add()
test_lower_corner_subtract()
test_upper_corner_add()
test_upper_corner_subtract()


''' 
Test cases
    Normal addition
    Normal subtraction
    Lower edge add (0 and -1)
    Upper edge add (9 and 10)
    Lower edge subtract (0 and -1)
    Upper edge subtract (9 and 10)
'''