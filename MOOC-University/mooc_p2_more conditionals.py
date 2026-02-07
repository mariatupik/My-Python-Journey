# Programming exercise: age of maturity
age = int(input("How old are you?"))
if age < 18:
    print("You are not of age!")
else:
    print("You are of age!")

# Programming exercise: greater than or equal to
number1 = int(input("Please type in the first number: "))
number2 = int(input("Please type in another number:"))
if number1 < number2:
    print(f"The greater number was: {number2}")
elif number1 > number2:
    print(f"The greater number was: {number1}")
else:
    print("The numbers are equal!")

# Programming exercise: the elder
name1 = input("Person 1: ")
age1 = int(input("Age 1: "))
name2 = input("Person 2: ")
age2 = int(input("Age 2: "))
if age1 > age2:
    print(f"The elder is {name1}")
elif age2 > age1:
    print(f"The elder is {name2}")
else:
    print(f"{name1} and {name2} are the same age")

# Programming exercise: alphabetically last
word1 = input("Please type in the 1st word: ")
word2 = input("Please type in the 2st word: ")
if word1 > word2:
    print(f"{word1} comes alphabetically last.")
elif word1 < word2:
    print(f"{word2} comes alphabetically last.")
elif word1 == word2:
    print("You gave the same word twice.")

# Programming exercise: age check
age = int(input("What is your age?"))
if age >= 5:
    print(f"Ok, you're {age} years old")
elif 0 <= age < 5:
    print(f"I suspect you can't write quite yet...")
else:
    print("That must be a mistake")

# Programming exercise: nephews
name = input("Please type in your name:")
if name == "Morty" or name == "Ferdie":
    print("I think you might be one of Mickey Mouse's nephews.")
elif name == "Huey" or name== "Dewey" or name == "Louie":
    print("I think you might be one of Donald Duck's nephews.")
else:
    print("You're not a nephew of any character I know of.")

# Programming exercise: grades and points

points = float(input("How many points [0-100]: "))
if points < 0 or points > 100:
    print("impossible!")
elif 90 <= points <= 100:
    print(f"Grade: 5")
elif  80 <= points <= 89:
    print(f"Grade: 4")
elif 70 <= points <= 79:
    print(f"Grade: 3")
elif 60 <= points <= 69:
    print(f"Grade: 2")
elif 50 <= points <= 59:
    print(f"Grade: 1")
elif 0 <= points <= 49:
    print("fail")

# Programming exercise: FizzBuzz
number = int(input("Number:"))
if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print ("Fizz")
elif number % 5 == 0:
   print ("Buzz")

#Programming exercise:leap year
year = int(input("Please type in a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("That year is a leap year.")
else:
    print("That year is not a leap year.")

# Programming exercise: alphabetically in the middle
letter1 = input("1st letter: ")
letter2 = input("2nd letter: ")
letter3 = input("3nd letter: ")
if letter2 < letter1 < letter3 or letter3 < letter1 < letter2:
    print(f"The letter in the middle is {letter1}")
elif letter1 < letter2 < letter3 or letter3 < letter2 < letter1:
    print(f"The letter in the middle is {letter2}")
elif letter1 < letter3 < letter2 or letter2 < letter3 < letter1:
    print(f"The letter in the middle is {letter3}")

# Programming exercise: gift tax calculator
value = int(input("Value of gift: "))
if 5000 <= value < 25000:
    print(f"Amount of tax: {100 + (value - 5000)*0.08} euros")
elif 25000 <= value < 55000:
    print(f"Amount of tax: {1700 + (value - 25000)*0.1} euros")
elif 55000 <= value < 200000:
    print(f"Amount of tax: {4700 + (value - 55000)*0.12} euros")
elif 200000 <= value < 1000000:
    print(f"Amount of tax: {22100 + (value - 200000)*0.15} euros")
elif value >= 1000000:
    print(f"Amount of tax: {142100 + (value - 1000000)*0.17} euros")
else:
    print("No tax!")