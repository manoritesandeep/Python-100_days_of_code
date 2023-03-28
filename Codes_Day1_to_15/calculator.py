from replit import clear
from calculator_art import logo

# Define mathematical operations into functions
def add(n1:float, n2:float):
    """
    Add two numbers and return their sum. 
    """
    return n1 + n2

def subtract(n1:float, n2:float):
    """
    Subtract two numbers and return their result. 
    """
    return n1 - n2

def multiply(n1:float, n2:float):
    """
    Multiply two numbers and return their result. 
    """
    return n1 * n2

def divide(n1:float, n2:float):
    """
    Divide two numbers and return their result. 
    """
    return n1 / n2

def exponential(n1:float, n2=1):
    """
    Square a numbers and return the result. 
    Please enter your number in num1. 
    """
    return n1 * n1

# # Test functions functionality
# print(subtract(3.5,5.5))
# print(divide(5,3))
# print(square(2.2))

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
    "^":exponential
    }

# using Recursion - A function calling itself
def calculator():
    print(logo)
    num1 = float(input("Enter the first number: "))
    # num1, num2 = 4,2
    for symbol in operations:
        print(symbol)
    
    should_continue = True
    while should_continue:
        operation_symbol = input(f"Pick an operation to perform from the following options: ")
        num2 = float(input("Enter the next number: "))
        calculation_func = operations[operation_symbol]
        answer = calculation_func(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer} or type 'n' to start fresh.:").lower() == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()