#Name : Ian Karanja Kamamo
#Reg.No.: Sct211-0461/2022

height = float(input("Please enter your height in meters: "))# in meters e.g. 1.69
weight = int(input("Please enter your weight in kilograms: "))# in kgs e.g. 78

bmi = weight / (height * height)

if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
else:
  print(f"Your BMI is {bmi}, you are overweight.")

