
        # Perform the selected operation
        if operator == '+':
            result = add(num1, num2)
            if result is not None:
                print(f"Result: {num1} + {num2} = {result}")
        elif operator == '-':
            result = subtract(num1, num2)
            if result is not None:
                print(f"Result: {num1} - {num2} = {result}")
        else:
            print("Invalid operator. Please enter + to add or - to subtract.")

    except ValueError as ve:
        print(f"Invalid input. Please enter a valid number. Error: {ve}")
    except ZeroDivisionError as zde:
        print(f"Error: Division by zero. {zde}")

# Call the calculator function
calculator()
