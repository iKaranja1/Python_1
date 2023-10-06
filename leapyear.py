#Name: Ian Karanja Kamamo
#Registration no.: Sct211-0461/2022
#LEAP YEAR PROGRAM

year = int(input("Which year do you want to check? "))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("It is a Leap year")
    else:
      print("It is not a leap year")
  else:
    print("It is a leap year")
else:
  print("it is not a leap year")
