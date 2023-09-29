#Name : Ian Karanja Kamamo
#Registartion no.: Sct211-0461/2022

print("Welcome to the tip calculator.")
bill = int(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))

percent100 = (tip / 100) + 1
split = int(input("How many people to split the bill? "))

pay = round((bill * percent100)/split, 2)

print(f"Each person should pay: ${pay}")

