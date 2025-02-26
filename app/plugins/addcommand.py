from decimal import Decimal, InvalidOperation
from app.calculator import Calculator
from app.commands import Command

class Add(Command):
    """
    Command to perform addition on two Decimal numbers.
    """
    def __init__(self, command_handler):
        self.command_handler = command_handler

    def execute(self, *args):
        """
        Executes the addition command. If no arguments are provided,
        it prompts the user to enter two numbers.
        """
        # Prompt for input if no arguments are given
        if not args:
            user_input = input("Enter two numbers separated by space: ")
            args = user_input.split()

        # Ensure exactly two arguments are provided
        if len(args) != 2:
            print("Only two arguments must be given")
            return

        try:
            num1, num2 = map(Decimal, args)
            outcome = Calculator.add(num1, num2)
            print(f"{num1} + {num2} = {outcome}")
        except InvalidOperation:
            print("One of the entered numbers is invalid. Please enter valid inputs.")
        except Exception as error:
            print(f"{error}")
