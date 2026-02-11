# Programming exercise: string multiplied
word = input("Please type in a string:")
number = int(input("Please type in an amount:"))
res = (f"{word*number}")
print(res)

# Programming exercise: the longer string
word1 = input("Please type in string 1:")
word2 = input("Please type in string 2:")
if len(word1) > len(word2):
    print(f"{word1} is longer")
elif len(word1) < len(word2):
    print(f"{word2} is longer")
else:
    print("The strings are equally long")

# Programming exercise: end to beginning
input_string = (input("Please type in a string: "))
index = len(input_string) - 1
while index >= 0:
    print(input_string[index])
    index -= 1

# Programming exercise: second and second to last characters
input_string = input("Please type in a string: ")
if (input_string [1]) != (input_string [-2]):
    print ("The second and the second to last characters are different")
elif (input_string [1]) == (input_string [-2]):
    print(f"The second and the second to last characters are {input_string [1]}")

# Programming exercise: a line of hashes
input_string = int(input("Width: "))
print("#"*input_string)

#Programming exercise: a rectangle of hashes
input_string = int(input("Width: "))
height = int(input("Height: "))
line_count = 0
while line_count < height:
    print("#" * input_string)
    line_count += 1

# Programming exercise: underlining
while True:
    input_string = input("Please type in a string: ")
    if len(input_string) == 0:
        break
    else:
        print(input_string)
        print("-"*len(input_string))

# Programming exercise: right-aligned
input_string = input("Please type in a string: ")
symbol = 20 - len(input_string)
print("*"*symbol + input_string)

# Programming exercise: a framed word
input_string = input("Word:")
space = 28 - len(input_string)
left = space//2
right= space - left
print("*"*30)
print("*"+" "*left+input_string +" " *right+"*")
print("*"*30) 

# Programming exercise: substrings, part 1
string = input("Please type in a string:")
length = 1
while length <= len(string):
    print(string[0:length])
    length += 1

# Programming exercise: substrings, part 2
string = input("Please type in a string:")
length = 1
while length <= len(string):
    print(string[-length:])
    length += 1

# Programming exercise: does it contain vowels
substring = input("Please type in a string:")
if "a" in substring:
    print("a found")
else:
    print("a not found")
if "e" in substring:
    print("e found")
else:
    print("e not found")
if "o" in substring:
    print("o found")
else:
    print("o not found")

# Programming exercise: find the first substring
substring = input("Please type in a word:")
character = input("Please type in a character:")
index = substring.find(character)
if index != -1 and index + 3 <= len(substring):
    print(substring[index : index + 3])

# Programming exercise: find all the substrings
substring = input("Please type in a word:")
character = input("Please type in a character:")
index = substring.find(character)
while index != -1:
    if index + 3 <= len(substring):
        print(substring[index : index + 3])
    index = substring.find(character, index + 1)

# Programming exercise: the second occurrence
string = input("Please type in a string:")
substring = input("Please type in a substring:")
index1 = string.find(substring)
if index1 != -1:
    index2 = index1 + len(substring)
    final_index = string.find(substring, index2)
    if final_index != -1:
        print(f"The second occurrence of the substring is at index {final_index}.")
    else:
        print("The substring does not occur twice in the string.")
else:
    print("The substring does not occur twice in the string.")

