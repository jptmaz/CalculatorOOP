# Import class
from Calc_userinput import User_Input
from Calc_prog import calculator

def main():
    ui = User_Input()
    Calc = calculator()
    
    while(True):
        
        print("""Welcome to Calkie your program calculator! 
To begin, Calkie is asking you for two numbers!""")
        # Ask user for numbers 1 & 2
        number_1 = ui.input_user()
        number_2 = ui.input_user()
    
        # Ask user for operation
        print ("""[[[''''''' OPERATIONS ''''''']]]
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Exit""")
    
        command = input(str("Enter the number of the operation that you wish to do: "))
        if command == "1":
            Calc.addition(number_1, number_2)
        elif command == "2":
            Calc.subtraction(number_1, number_2)
        elif command == "3":
            Calc.multiplication(number_1, number_2)
        elif command == "4":
            Calc.division(number_1, number_2)

        elif command == "5":
            break
        else:
            print("I do not understand would you like to try again? YES or NO?")
            tryagain_calc = input("= ").upper()
            if tryagain_calc == "YES":
                True
            elif tryagain_calc == "NO":
                break

if __name__ == "__main__":
    main()