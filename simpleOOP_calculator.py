class Calculator:
    def __init__(self):
        pass

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 == 0:
            return "Cannot divide by zero"
        return num1 / num2
calc = Calculator()

while True:
    print("Options:")
    print("Enter '+' for addition")
    print("Enter '-' for subtraction")
    print("Enter '*' for multiplication")
    print("Enter '/' for division")
    print("Enter 'quit' to end the program")

    user_input = input(": ")

    if user_input == "quit":
        break
    elif user_input in ["+", "-", "*", "/"]:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if user_input == "+":
            result = calc.add(num1, num2)
        elif user_input == "-":
            result = calc.subtract(num1, num2)
        elif user_input == "*":
            result = calc.multiply(num1, num2)
        elif user_input == "/":
            result = calc.divide(num1, num2)

        print("Result: " + str(result))
    else:
        print("Invalid input")
