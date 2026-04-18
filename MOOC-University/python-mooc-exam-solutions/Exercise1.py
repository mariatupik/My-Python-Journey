all_string = ""
while True:
    user_string = input("Enter a string: ")
    if user_string == "":
        break
    else:
        all_string += user_string

user_number = int(input("Minimum number of characters: "))
all_characters = {}

for ch in all_string:
    if ch not in all_characters:
        all_characters[ch] = 1
    else:
        all_characters[ch] += 1

filtered_characters = []
for ch, number in all_characters.items():
    if number >= user_number:
        filtered_characters.append([number, ch])

sorted_characters = sorted(filtered_characters)
final_list = sorted_characters[::-1]

print("Characters in order of occurrence:")
for number, ch in final_list:
    print(f'  Character "{ch}" was entered {number} times')