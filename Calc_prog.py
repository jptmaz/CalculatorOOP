# Create a class
class calculator():
    # Create a special init method
    def __init__(self, sum = 0, difference = 0, product = 0, quotient = 0):
        # Select all instance variables
        self.sum = sum
        self.difference = difference
        self.product = product
        self.quotient = quotient
    # Create method for addition operation
    def addition(self, number_1, number_2):
        while(True):
            sum = float(number_1) + float(number_2)
            message = f"The sum of {number_1} and {number_2} is {sum}"
            print(message)
            print("__ __________ __")
            try_again = input("Do you want to try again? YES or NO: ").upper()
            if try_again == "YES":
                break
            elif try_again == "NO":
                exit()
            else:
                print("Calkie did not understand you, try again.")
                True
                
    # Create method for subtraction
    def subtraction(self, number_1, number_2):
        while(True):
            difference = float(number_1) - float(number_2)
            message = f"The difference of {number_1} and {number_2} is {difference}"
            print(message)
            print("__ __________ __")
            try_again = input("Do you want to try again? YES or NO: ").upper()
            if try_again == "YES":
                break
            elif try_again == "NO":
                exit()
            else:
                print("Calkie did not understand you, try again.")
                True
                
    # Create method for multiplication
    def multiplication(self, number_1, number_2):
        while(True):
            product = float(number_1) * float(number_2)
            message = f"The sum of {number_1} and {number_2} is {product}"
            print(message)
            print("__ __________ __")
            try_again = input("Do you want to try again? YES or NO: ").upper()
            if try_again == "YES":
                break
            elif try_again == "NO":
                exit()
            else:
                print("Calkie did not understand you, try again.")
                True
    # Create method for division
    def division(self, number_1, number_2):
        while(True):
            quotient = float(number_1) / float(number_2)
            message = f"The sum of {number_1} and {number_2} is {quotient}"
            print(message)
            print("__ __________ __")
            try_again = input("Do you want to try again? YES or NO: ").upper()
            if try_again == "YES":
                break
            elif try_again == "NO":
                exit()
            else:
                print("Calkie did not understand you, try again.")
                True  
        
 