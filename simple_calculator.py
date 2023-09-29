#Name : Ian Karanja Kamamo
#Registartion no.: Sct211-0461/2022
value1 = float(input("Enter the first value: "))
value2 = float(input("Enter the second value: "))

operation = int(input("Choose the number of the operator(1,2,3 or 4)\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n:"))

if operation == 1:
    answer = value1 + value2
    print(f"{value1} + {value2} = {answer}")

elif operation == 2:
    answer = value1 - value2
    print(f"{value1} - {value2} = {answer}")

elif operation == 3:
    answer = value1 * value2
    print(f"{value1} * {value2} = {answer}") 

elif operation == 4:
    answer = value1 / value2
    print(f"{value1} / {value2} = {answer}")

else:
    print("Invalid input.")
