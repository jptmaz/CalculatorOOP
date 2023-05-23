# Create a class
class User_Input():
    # Create method for first number 
    def input_user(self):
        try:
            number = float(input("Enter the number: "))
        except ValueError:
            print("An error has occured, please try again.")
            number = float(input("Enter a number again: "))
        
        return number