# EProgramming exercise: Orwell - print message if input equals 1984
number = int(input("Please type in a number: "))
if number == 1984:
    print("Orwell")

# Programming exercise: Absolute Value

number = int(input("Please type in a number:"))
if number >= 0:
    print(f"The absolute value of this number is {number}")
if number < 0:
    print (f"The absolute value of this number is {number*-1}")

# Programming exercise: Soup or no soup

user_name = input("Please tell me your name: ")
if user_name != "Jerry":
    total = int(input("How many portions of soup? "))
    print(f"The total cost is {total * 5.90}")
print("Next please!")

# Programming exercise:Order of magnitude

number = int(input("Please type in a number: "))
if 100 <= number < 1000:
    print("This number is smaller than 1000")
   
if 10<= number < 100:
    print("This number is smaller than 1000")
    print("This number is smaller than 100")
    
if number <10:
    print("This number is smaller than 1000")
    print("This number is smaller than 100")
    print("This number is smaller than 10")
print("Thank you!")

#Programming exercise:Calculator
number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))
operation = input("Operation: ")
if operation == "add":
    print(f"{number1} + {number2} = {number1+number2}")
if operation == "multiply":
    print(f"{number1} * {number2} = {number1*number2}")
if operation == "subtract":
    print(f"{number1} - {number2} = {number1-number2}")

# Programming exercise:Temperatures
degrees_f = int(input("Please type in a temperature (F): "))
degrees_c = int(degrees_f-32)/1.8
print(f"{degrees_f}  degrees Fahrenheit equals {degrees_c} degrees Celsius")
if degrees_c < 0:
    print("Brr! It's cold in here!")

# Programming exercise: Daily wages
hourly_wage = float(input("Hourly wage: "))
hours_worked = int(input("Hours worked: "))
day = input("Day of the week: ")
if day != "Sunday":
    print(f"Daily wages: {hourly_wage*hours_worked} euros")
if day == "Sunday":
    print(f"Daily wages: {hourly_wage*hours_worked*2} euros")

# Programming exercise: Loyalty bonus
points = int(input("How many points are on your card? "))
new_points = points
if new_points < 100:
    points *= 1.1
    print("Your bonus is 10 %")
    print("You now have", points, "points")
if new_points >= 100:
    points *= 1.15
    print("Your bonus is 15 %")
    print("You now have", points, "points")

# Programming exercise: What to wear tomorrow
degrees = int(input("What is the weather forecast for tomorrow? "))
rain = input("Will it rain (yes/no): ")
if 11 < degrees > 20:
    print("Wear jeans and a T-shirt")
if 10 < degrees <= 20:
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
if degrees <= 10:
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
    print("Take a jacket with you")
if degrees < 10:
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
    print("Take a jacket with you")
    print("Make it a warm coat, actually")
    print("I think gloves are in order")
if rain == "yes":
    print("Don't forget your umbrella!")

#Programming exercise: Solving a quadratic equation

from math import sqrt
a = float(input("Value of a: "))
b = float(input("Value of b: "))
c = float(input("Value of c: "))

roat1 = (-b+sqrt(b**2-4*a*c))/(2*a)
roat2 = (-b-sqrt(b**2-4*a*c))/(2*a)
print(f"The roots are {roat1} and {roat2}")