# Programming exercise: shall we continue?
while True:
    print("hi")
    answer = input("Shall we continue? ")
    if answer == "no":
        break
print("okay then")

# Programming exercise: input validation
from math import sqrt
while True:
    number = int(input("Please type in a number: "))
    if number == 0:
        print("Exiting...")
        break
    if number < 0:
        print("Invalid number")
    else:
        print(sqrt(number))
# Programming exercise: fix the code: Countdown
print("Countdown!")
number = 5
while True:
    print(number)
    number = number-1
    if number == 0:
        break

print("Now!")

#Programming exercise: repeat password
password = input("Password: ")
repeat = input("Repeat password:")  
password == repeat
while True:
    if password != repeat:
        print("They do not match!")
        repeat = input("Repeat password:")
    elif password == repeat:
        break

print("User account created!")

# Programming exercise: PIN and number of attempts
attempts = 0
while True:
    code = input("PIN:")
    attempts += 1
    if code == "4321":
        if attempts == 1:
            print("Correct! It only took you one single attempt!")
        else:
            print(f"Correct! It took you {attempts} attempts")
        break 
    else:
        print("Wrong")

# Programming exercise: the next leap year

year = int(input("Year: "))
current_year = year
while True:
    current_year += 1
    if (current_year % 4 == 0 and current_year % 100 != 0) or (current_year % 400 == 0):
        print(f"The next leap year after {year} is {current_year}")
        break

# Programming exercise: story
words = ""
last_word = "" 
while True:
    word = input("Please type in a word: ")
    
    if word == "end" or word == last_word:
        break
    
    words += word + " "
   
    last_word = word

print(words.strip())

# Programming exercise: working with numbers
print("Please type in integer numbers. Type in 0 to finish.")
count = 0
total_sum = 0
positives = 0
negatives = 0
while True:
    number = int(input("Number: "))
    if number == 0:
       break
    count += 1
    total_sum += number
    if number > 0:
        positives += 1
    else:
        negatives += 1
print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {total_sum}")
if count > 0:
    mean = total_sum / count
    print(f"The mean of the numbers is {mean}")

print(f"Positive numbers {positives}")
print(f"Negative numbers {negatives}")