from datetime import date;

user_Date_Of_Birth = int(input("Enter year in which you born: "))

currentDate = date.today()
currentYear = currentDate.year

user_Age = currentYear - user_Date_Of_Birth
print("Your Age Is: ", user_Age)