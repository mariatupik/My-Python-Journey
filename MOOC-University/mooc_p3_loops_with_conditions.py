# Programming exercise: print numbers
number = 2
while number <= 30:
    if number% 2 == 0:
        print(number)
    number += 1

# Programming exercise: fix the code: Countdown
print("Are you ready?")
number = int(input("Please type in a number: "))
while number != 0:
    print(number)
    number -= 1
print("Now!")

# Programming exercise: numbers

first_number = int(input("Upper limit: "))
number = 1
while number <= first_number-1:
    print(number)
    number += 1

# Programming exercise: powers of two
limit = int(input("Upper limit:"))
number = 1
while number <= limit:
    print(number)
    number *= 2

# Programming exercise: powers of base n
limit = int(input("Upper limit:"))
base = int(input("Base: "))
number = 1
while number <= limit:
    print(number)
    number *= base

# Programming exercise: the sum of consecutive numbers, version
limit = int(input("Limit: "))
number = 1
result_sum = 0 
while result_sum < limit:
    result_sum += number
    number += 1
print(result_sum)

# Programming exercise: the sum of consecutive numbers, version 2
limit = int(input("Limit: "))
number = 1
result_sum = 1
steps = "1"
while result_sum < limit:
    number += 1 
    result_sum += number
    steps += f" + {number}" 
print(f"The consecutive sum: {steps} = {result_sum}")