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
        sum = number_1 + number_2
        message = f"The sum of {number_1} and {number_2} is {sum}"
        print(message)
        print("__ __________ __")
        print("Would you like to try again?")
        while(True):
            try_again = input(str("= ")).upper()
            if try_again == "YES":
                True
            elif try_again == "NO":
                break
            else:
                print("I do not understand would you like to try again? YES or NO?")
                tryagain_error = input("= ").upper()
                if tryagain_error == "YES":
                    True
                else:
                    print("I do not understand. Let's start at the beginning.")
                    break      
    # Create method for subtraction
    def subtraction(self, number_1, number_2):
        difference = number_1 - number_2
        message = f"The difference of {number_1} and {number_2} is {difference}"
        print(message)
        print("__ __________ __")
        print("Would you like to try again?")
        while(True):
            try_again = input(str("= ")).upper()
            if try_again == "YES":
                True
            elif try_again == "NO":
                break
            else:
                print("I do not understand would you like to try again? YES or NO?")
                tryagain_error = input("= ").upper()
                if tryagain_error == "YES":
                    True
                else:
                    print("I do not understand. Let's start at the beginning.")
                    break    
    # Create method for multiplication
    def multiplication(self, number_1, number_2):
        product = number_1 * number_2
        message = f"The product of {number_1} and {number_2} is {product}"
        print(message)
        print("__ __________ __")
        print("Would you like to try again?")
        while(True):
            try_again = input(str("= ")).upper()
            if try_again == "YES":
                True
            elif try_again == "NO":
                break
            else:
                print("I do not understand would you like to try again? YES or NO?")
                tryagain_error = input("= ").upper()
                if tryagain_error == "YES":
                    True
                else:
                    print("I do not understand. Let's start at the beginning.")
                    break    
    # Create method for division
    def division(self, number_1, number_2):
        quotient = number_1 / number_2
        message = f"The sum of {number_1} and {number_2} is {quotient}"
        print(message)
        print("__ __________ __")
        print("Would you like to try again?")
        while(True):
            try_again = input(str("= ")).upper()
            if try_again == "YES":
                True
            elif try_again == "NO":
                break
            else:
                print("I do not understand would you like to try again? YES or NO?")
                tryagain_error = input("= ").upper()
                if tryagain_error == "YES":
                    True
                else:
                    print("I do not understand. Let's start at the beginning.")
                    break   