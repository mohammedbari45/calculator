import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def print_menu():
    print("Option 1: Division\nOption 2: Multiplication\nOption 3: Addition\nOption 4: Subtraction\nOption 5: Exponentiation\n6: Exit")
def add(x, y):
    return x + y
def divide(x, y):
    while y == 0:
        y = int(input("You can't divide by zero, enter a different number! "))
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
        print_menu
        operation = int(input("What operation would you like to do " + name + "? "))
        while operation not in [1,2,3,4,5,6]:
            operation = int(input("Please select a valid option from the menu! "))
        clear_screen
        numberOne = int(input("Enter your first number! "))
        while numberOne 
        numberTwo = int(input("Enter your second number! "))
        if operation == 1:
            print("Your result is: " + divide(numberOne, numberTwo))
            nextStep = int(input("Would you like to 1. Exit or 2. Do another calculation: "))
            if nextStep != 1 or nextStep != 2:
                nextStep = int(input("Choose a valid option! "))
            if nextStep == 1:
                exit()
            elif nextStep == 2:
                continue
        elif operation == 2:
            print("Your result is: " + multiply(numberOne, numberTwo))
            nextStep = int(input("Would you like to 1. Exit or 2. Do another calculation: "))
            if nextStep != 1 or nextStep != 2:
                nextStep = int(input("Choose a valid option! "))
            if nextStep == 1:
                exit()
            elif nextStep == 2:
                continue
        elif operation == 3:
            print("Your result is: " + add(numberOne, numberTwo))
            nextStep = int(input("Would you like to 1. Exit or 2. Do another calculation: "))
            if nextStep != 1 or nextStep != 2:
                nextStep = int(input("Choose a valid option! "))
            if nextStep == 1:
                exit()
            elif nextStep == 2:
                continue
        elif operation == 3:
            print("Your result is: " + subtract(numberOne, numberTwo))
            nextStep = int(input("Would you like to 1. Exit or 2. Do another calculation: "))
            if nextStep != 1 or nextStep != 2:
                nextStep = int(input("Choose a valid option! "))
            if nextStep == 1:
                exit()
            elif nextStep == 2:
                continue
        elif operation == 3:
            print("Your result is: " + exponent(numberOne, numberTwo))
            nextStep = int(input("Would you like to 1. Exit or 2. Do another calculation: "))
            if nextStep != 1 or nextStep != 2:
                nextStep = int(input("Choose a valid option! "))
            if nextStep == 1:
                exit()
            elif nextStep == 2:
                continue

if __name__ == "__main__":
    main()
