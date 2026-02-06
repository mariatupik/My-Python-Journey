# Exercise: Arithmetic operations with x and y
x = 2
y = 15
print(f"{x} + {y} = {x+y}")
print(f"{x} - {y} = {x-y}")
print(f"{x} * {y} = {x*y}")
print(f"{x} / {y} = {x/y}")

# Exercise: Print combined operations (hardcoded)
x = 4
y = 9
print(5, end = "")
print(" + ", end = "")
print(8, end = "")
print(" - ", end = "")
print(4, end = "")
print(" = ", end = "")
print(5 + 8 - 4)

# Exercise: Multiply by five

number = int(input("Please type in a number:"))
print(f"{number} times 5 is {number*5}")

# Exercise: Age calculator

name = input("What is your name? ")
age = int(input("Which year were you born?"))
print(f"Hi {name}, you will be {2021 - age} years old at the end of the year 2021")

# Exercise: Seconds in days

days = int(input("How many days?"))
print(f"Seconds in that many days: {days*24*60*60}")

# Exercise: Product of three numbers

number1 = int(input("Please type in the first number: "))
number2 = int(input("Please type in the second number: "))
number3 = int(input("Please type in the third number: "))
product = number1 * number2 * number3
print(f"The product is {product}")

# Exercise: Sum and product of two numbers

number1 = int(input("Number 1:"))
number2 = int(input("Number 2:"))
print(f"The sum of the numbers: {number1+number2}")
print(f"The product of the numbers: {number1*number2}")

# Exercise: Sum and mean of four numbers

number1 = int(input("Number 1:"))
number2 = int(input("Number 2:"))
number3 = int(input("Number 3:"))
number4 = int(input("Number 4:"))
print(f"The sum of the numbers is {number1+number2+number3+number4} and the mean is {(number1+number2+number3+number4)/4}")

# Exercise: Student cafeteria budget

times_a_week = int(input("How many times a week do you eat at the student cafeteria?"))
price_of_lunch = float(input("The price of a typical student lunch?"))
groceries = float(input("How much money do you spend on groceries in a week?"))
print("Average food expenditure:")
print(f"Daily: {(groceries+times_a_week * price_of_lunch)/7} euros")
print(f"Weekly: {groceries+times_a_week * price_of_lunch} euros")
students = int(input("How many students on the course?"))
size = int(input("Desired group size?"))
print(f"Number of groups formed: {(students + size - 1) // size}")