#Programming exercise: fix the syntax
number = int(input("Please type in a number: "))
if number <= 100:
    print(f"{number} must be my lucky number!")
if number > 100:
    print("The number was greater than one hundred")
    print("Now its value has decreased by one hundred")
    print(f"Its value is now {number - 100}")
    print(f"{number - 100} must be my lucky number!")
print("Have a nice day!")

# Programming exercise: number of characters

word = input("Please type in a word: ")
letters = len(word)
if letters != 1:
    print(f"There are {letters} n the word {word}")
print("Thank you!")

# Programming exercise: typecasting

number = float(input("Please type in a number: "))
print(f"Integer part: int({number})")
print(f"Decimal part: float({float(number)-int(number)}")