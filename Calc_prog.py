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
    def sum(self, number_1, number_2):
        sum = number_1 + number_2
        message = f"The sum of {number_1} and {number_2} is {sum}"
        print(message)
    # Create method for subtraction
    def difference(self, number_1, number_2):
        difference = number_1 - number_2
        message = f"The difference of {number_1} and {number_2} is {difference}"
        print(message)
    # Create method for multiplication
    def product(self, number_1, number_2):
        product = number_1 * number_2
        message = f"The product of {number_1} and {number_2} is {product}"
        print(message)
    # Create method for division
    def quotient(self, number_1, number_2):
        quotient = number_1 / number_2
        message = f"The sum of {number_1} and {number_2} is {quotient}"
        print(message)