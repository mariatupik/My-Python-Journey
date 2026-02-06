# LESSON 2: Variables, Types and Math
#1. Variable reassignment and deletion
user_name = input('Enter your name: ')
print('Hello, ', user_name, '!', sep="")
info = 50
print('Result: ', info, '!', sep='') # Using empty separator
del info # Removing variable from memory
info = 7 # Re-creating the same variable name with a new value
print("New info:", info)

# 2. Type Annotation and Type Casting
a1: int = 50
a2: float = 5.34
a3: str = '5' 
a4: bool = False

# Converting string to int to perform addition
print("Addition (int + int):", a1 + int(a3)) 
print("Addition (float + float):", float(a1) + float(a3))

# 3. Boolean Logic
a5 = 0
print("Is 0 True or False?", bool(a5)) # 0 is always False in Python

# 4. Multiple Assignment
x, y, z = 5, True, False # Assigning different values to different variables
a = b = 10.5             # Assigning the same value to two variables
a = "some"               # Dynamic typing: 'a' was a float, now it's a string

# 5. Arithmetic Operations
num1 = 5
num2 = 10.5
print("Sum:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Remainder:", num1 % num2)

# 6. Shorthand Assignment
num1 -= 10 # Equivalent to: num1 = num1 - 10
print("Updated num1:", num1)

# 7. Getting input (input() is ALWAYS a string initially)
num1 = int(input('Enter num 1: ')) # Converting directly
num2 = input('Enter num 2: ')      # Still a string here

# 8. Operations with type conversion
print("Addition:", num1 + int(num2))

# 9. Advanced Math Operators
print("Power (num1^num2):", num1 ** int(num2))
print("Floor Division:", num1 // int(num2))