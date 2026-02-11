# Programming exercise: multiplication
number = int(input("Please type in a number:"))
for number2 in range(1, number + 1):
    for number3 in range(1, number + 1):
        print(f"{number2} x {number3} = {number2 * number3}")

# Programming exercise: first letters of words       
sent = input("Please type in a sentence:")
index = 0
print(sent[index])
while index < len(sent):
    if sent[index] == " ":
        print(sent[index+1])
    index += 1

# Programming exercise: Factorial
import math 
while True:
    number = int(input("Please type in a number:"))
    if number <= 0:
        break
    fact = math.factorial(number)  
    print(f"The factorial of the number {number} is {fact}")

print("Thanks and bye!")

# Programming exercise: flip the pairs

number = int(input("Please type in a number:"))
i = 1
while i <= number:
    if  i+1 <= number:
        print(i+1)
        print(i)
    else:
        print(i)
    
    i += 2

# Programming exercise: taking turns
number = int(input("Please type in a number:"))
i = 1
y = number
while i <= y:
    print(i)
    i+=1
    if i <= y:
        print(y)
        y-=1   