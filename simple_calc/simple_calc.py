from contracts import contract

class Calc():
    def __init__(self):
        self.result = None
    @contract(operand1='int,>=0,<10', operand2='int,>=0,<10', returns='int')
    def add(self, operand1, operand2):
        """
        Adds two integers between 0 and 9
        :param operand1:
        :param operand2:
        :return:
        """
        self.result = operand1 + operand2
        return self.result

    @contract(operand1='int,>=0,<10', operand2='int,>=0,<10', returns='int')
    def subtract(self, operand1, operand2):
        """
        Subtracts two integers between 0 and 9
        :param operand1:
        :param operand2:
        :return:
        """
        self.result = operand1 - operand2
        return self.result