# Programming exercise: Seven Brothers
def seven_brothers():
    print("Aapo")
    print("Eero")
    print("Juhani")
    print("Lauri")
    print("Simeoni")
    print("Timo")
    print("Tuomas")
if __name__ == "__main__":    
    seven_brothers()

#Programming exercise:The first character
def first_character(text):
    print(text[0])
    
if __name__ == "__main__":
    first_character('python')
    first_character('yellow')
    first_character('tomorrow')
    first_character('heliotrope')
    first_character('open')
    first_character('night')

# Programming exercise: Mean
def mean(x, y, c):
    reasalt = ((x+y+c)/3)
    print(float(reasalt))
if __name__ == "__main__":
    print(mean(1, 2, 3))

# Programming exercise: Print many times
def print_many_times(text, times):
    while times > 0:
        print(text)
        times -= 1
if __name__ == "__main__":
    print_many_times("python", 5)

# Programming exercise: A square of hashes
def hash_square(length):
    row = length
    while length>0:
        print("#"*row)
        length -= 1
if __name__ == "__main__":
    hash_square(5)
# Programming exercise: Chessboard
def chessboard(number):
    row = number
    i = 0
    while number > 0:
        if i % 2 == 0:
            print(("10" * row)[:row]) 
        else:
            print(("01" * row)[:row])   
        number -= 1
        i += 1
if __name__ == "__main__":
    chessboard(3)

# Programming exercise: A word squared
def squared(text, number):
    row=number
    whight = text*number*number
    start = 0
    while number > 0:
        print(whight[start : start + row])
        start+=row
        number -= 1

if __name__ == "__main__":
    squared("ab", 3)
    print()
    squared("aybabtu", 5)
