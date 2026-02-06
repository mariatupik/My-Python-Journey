# Exercise: Basic print

print('Hi there!')

print(":-)")

# Exercise: Seven Brothers
print("Aapo")
print("Eero")
print("Juhani")
print("Lauri")
print("Simeoni")
print("Timo")
print("Tuomas")

# Exercise: Row your boat
print("Row, row, row your boat,")
print("Gently down the stream.")
print("Merrily, merrily, merrily, merrily,")
print("Life is but a dream.")

# Exercise: Minutes in a year
print(365 * 24 * 60)

# Exercise: Print code as string
print('print("Hello there!")')

# Exercise: Repeat name twice
user_name = input("What is uour name?")
print(user_name)
print(user_name)

# Exercise: Name with exclamation marks
user_name = input("What is your name?")
print("!" + user_name + "!" + user_name + "!")

# Exercise: Contact details
given_name = input("What is your given name?")
family_name = input("What is your family name?")
street_address = input("What is your street address?")
city_and_postal_code = input ("What is your city and postal code?")
print(given_name , family_name)
print(street_address)
print(city_and_postal_code)

# Exercise: Combining parts
part_1st = input("The 1st part: ")
part_2st = input("The 1st part: ")
part_3st = input("The 1st part: ")
print(part_1st +"-" + part_2st + "-" + part_3st + "!")

# Exercise: Story (Knight)
name = input("Please type in a name: ")
year = input("Please type in a year: ")
print(name + " is a valiant knight, born in the year " + year + ".")
print("One morning " + name + " woke up to an awful racket: a dragon was approaching the village.")
print("Only " + name + " could save the village's residents.")

# Exercise: Professional Profile
name = "Tim Tester"
age = 20
skill1 = "python"
level1 = "beginner"
skill2 = "java"
level2 = "veteran"
skill3 = "programming"
level3 = "semiprofessional"
lower = 2000
upper = 3000

print(f"my name is {name}, I am {age} years old\n")
print("my skills are")
print(f" - {skill1} ({level1})")
print(f" - {skill2} ({level2})")
print(f" - {skill3} ({level3})\n")
print(f"I am looking for a job with a salary of {lower}-{upper} euros per month")