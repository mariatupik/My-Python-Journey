# hello_visual_studio_code
while True:
    current_editor = input("Which code editor do you use? ")
    current_editor = current_editor.lower()
    if current_editor == "visual studio code":
        print("an excellent choice!")
        break
    elif current_editor == "notepad" or current_editor == "word":
        print("awful")
    else:
        print("not good")

# Line
def line(length, character):
    if character == "":
        character = "*" 
    else:
        character = character[0]
    for i in range(length):
        print(character, end="")
    print()

if __name__ == "__main__":
    line(5, "x")
    line(5, "")

# A box of hashes
def line(length, character):
    if character == "":
        character = "*" 
    else:
        character = character[0]
    for i in range(length):
        print(character, end="")
    print()

if __name__ == "__main__":
    line(5, "x")
    line(5, "")
    
def box_of_hashes(height):

    for i in range(height):
        line(10, "#")
 

if __name__ == "__main__":
    box_of_hashes(5)


# A square of hashes
def line(length, character):
    if character == "":
        character = "*" 
    else:
        character = character[0]
    for i in range(length):
        print(character, end="")
    print()
 
def square_of_hashes(size):
    for i in range(size):
        line(size, "#")
 
if __name__ == "__main__":
    square_of_hashes(5)

# A square

def line(length, character):
    if character == "":
        character = "*" 
    else:
        character = character[0]
    for i in range(length):
        print(character, end="")
    print()
def square(size, character):
    for i in range(size):
        line(size, character)
 
if __name__ == "__main__":
    square(5, "x")

# A triangle
def line(length, character):
    if character == "":
        character = "*" 
    else:
        character = character[0]
    for i in range(length):
        print(character, end="")
    print()
 
def triangle(size):
    for i in range(size):
        line(i + 1, "#")

if __name__ == "__main__":
    triangle(5)

# A shape
def line(length, character):
    if character == "":
        character = "*" 
    else:
        character = character[0]
    for i in range(length):
        print(character, end="")
    print()

def shape(size1, character1, size2, character2):
    for i in range(size1):
        line(i + 1, character1)
    for i in range(size2):
        line(size1, character2)
      
if __name__ == "__main__":
    shape(5, "x", 3, "o")
    
# A spruce
def line(length, character):
    if character == "":
        character = "*" 
    else:
        character = character[0]
    for i in range(length):
        print(character, end="")
    print()
 
def spruce(size):
    print("a spruce!")
    for i in range(size):
        spaces = size - i - 1
        print(" " * spaces, end="")
        line(2 * i + 1, "*")
    print(" " * (size - i - 1), end="")
    print(" " * (size - 1), end="")
    line(1, "*")
 

if __name__ == "__main__":
    spruce(5)

# The greatest number
def greatest_number(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    elif c >= a and c >= b:
        return c
    elif a == b == c:
        return a
 
if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)

# Same characters
def same_chars(word, char1, char2):
    if char1 <len(word) and char2<len(word):
        if word[char1] == word[char2]:
             return True
        else:
            return False
    else:
        return False
 
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))

# First, second and last words
def first_word(sentence):
    i = 0
    while sentence[i] != " ":
        i+=1
    return sentence[:i]
 
def second_word(sentence):
    i = 0
    while sentence[i] != " ":
        i += 1
    start = i + 1
    i = start
    while i < len(sentence) and sentence[i] != " ":
        i += 1
    return sentence[start:i]
 
def last_word(sentence):
    i = len(sentence) - 1
    while sentence[i] != " ":
        i-=1
    return sentence[i+1:]

if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))


