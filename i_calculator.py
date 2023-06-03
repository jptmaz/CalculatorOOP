from Calc_userinput import User_Input
from Calc_prog import calculator

class UserInput_Prog(User_Input):
    def input_user(self):
        return super().input_user()

class Calculator_Prog(calculator):
    def addition(self, number_1, number_2):
        return super().addition(number_1, number_2)
    
    def subtraction(self, number_1, number_2):
        return super().subtraction(number_1, number_2)
    
    def multiplication(self, number_1, number_2):
        return super().multiplication(number_1, number_2)
    
    def division(self, number_1, number_2):
        return super().division(number_1, number_2)
