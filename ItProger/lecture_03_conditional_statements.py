# Task: Practice with conditional statements and logical operators

# Part 1: Using 'and' (Both conditions must be true)
user_input = int(input("Enter a number: "))
has_car = True
if user_input == 5 and has_car:
    print("Condition met: Input is 5 and user has a car.")

 # Nested condition: This only runs if the 'if' above is true
    secondary_number = int(input("Enter number 10: "))
    if secondary_number == 10:
        print("Success! The number is 10.")
elif user_input == 3:
    print("Input is 3.")
else:
    print("No specific condition met for the first part.")

print("-" * 20) # Divider for clarity in console

# Part 2: Using 'or' and 'not'
user_input = int(input("Enter another number: "))
has_car = True
if user_input == 5 or has_car:
    print("Condition met: Either input is 5 or user has a car (or both).")

    secondary_number = int(input("Enter number 10: "))
    if secondary_number == 10:
        print("Success! The number is 10.")
elif -3 < user_input < 3 or not has_car:
    # This checks if number is between -3 and 3 OR if has_car is False
    print("Input is in range (-3, 3) or user does not have a car.")
else:
    print("Else branch reached.")


