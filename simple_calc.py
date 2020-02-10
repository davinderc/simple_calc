from contracts import contract

class Calc():
    def __init__(self):
        result = 0
    @contract(addend1='int,>=0,<10', addend2='int,>=0,<10', returns='int')
    def add(self, addend1, addend2):
        return addend1 + addend2

    @contract(operand1='int,>=0,<10', operand2='int,>=0,<10', returns='int')
    def subtract(self, operand1, operand2):
        return operand1 - operand2