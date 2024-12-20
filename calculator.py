import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def print_menu():
    print("Option 1: Division\nOption 2: Multiplication\nOption 3: Addition\nOption 4: Subtraction\nOption 5: Exponentiation\nOption 6: Exit")
def add(x, y):
    return x + y
def divide(x, y):
    while y == 0:
        y = int(input("You can't divide by zero, enter a different number: "))
    return x / y
def subtract(x,y):
    return x - y
def multiply(x, y):
    return x * y
def exponent(x,y):
    return x**y

def main():
    name = input("Welcome to my calculator, what's your name? ")
    while True:
        print_menu()
        operation = int(input("What operation would you like to do " + name + ": "))
        while operation not in [1,2,3,4,5,6]:
            operation = int(input("Please select a valid option from the menu: "))
        clear_screen()
        if operation == 6:
            print("Goodbye, see you next time " + name + "!")
            exit()
        try:
            numberOne = int(input("Enter your first number: "))
        except ValueError:
            numberOne = int(input("Please input a valid number: "))
        try:
            numberTwo = int(input("Enter your first number: "))
        except ValueError:
            numberTwo = int(input("Please input a valid number: "))

        if operation == 1:
            print("Your result is: " + str(divide(numberOne, numberTwo)))
            nextStep = int(input("Would you like to 1. Exit or 2. Do another calculation: "))
            while nextStep not in [1,2]:
                nextStep = int(input("Choose a valid option: "))
            if nextStep == 1:
                exit()
            elif nextStep == 2:
                clear_screen()
                continue
        elif operation == 2:
            print("Your result is: " + str(multiply(numberOne, numberTwo)))
            nextStep = int(input("Would you like to 1. Exit or 2. Do another calculation: "))
            while nextStep not in [1,2]:
                nextStep = int(input("Choose a valid option: "))
            if nextStep == 1:
                exit()
            elif nextStep == 2:
                clear_screen()
                continue
        elif operation == 3:
            print("Your result is: " + str(add(numberOne, numberTwo)))
            nextStep = int(input("Would you like to 1. Exit or 2. Do another calculation: "))
            while nextStep not in [1,2]:
                nextStep = int(input("Choose a valid option: "))
            if nextStep == 1:
                exit()
            elif nextStep == 2:
                clear_screen()
                continue
        elif operation == 4:
            print("Your result is: " + str(subtract(numberOne, numberTwo)))
            nextStep = int(input("Would you like to 1. Exit or 2. Do another calculation: "))
            while nextStep not in [1,2]:
                nextStep = int(input("Choose a valid option: "))
            if nextStep == 1:
                exit()
            elif nextStep == 2:
                clear_screen()
                continue
        elif operation == 5:
            print("Your result is: " + str(exponent(numberOne, numberTwo)))
            nextStep = int(input("Would you like to 1. Exit or 2. Do another calculation: "))
            while nextStep not in [1,2]:
                nextStep = int(input("Choose a valid option: "))
            if nextStep == 1:
                exit()
            elif nextStep == 2:
                clear_screen()
                continue
        elif operation == 6:
            print("Goodbye, see you next time " + name + "!")
            exit()

if __name__ == "__main__":
    main()
