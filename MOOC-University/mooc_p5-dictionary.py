# Times ten
def times_ten(start_index: int, end_index: int):
    new_dictionary = {}
    for i in range(start_index, end_index + 1):
        new_dictionary[i] = i * 10
    return new_dictionary
 
 
 
 
if __name__ == "__main__":
    d = times_ten(3, 6)
    print(d)

# Factorials
def factorials(n: int):
    new_dictionary = {}
    current_factorial = 1
    for i in range(1, n + 1):
        current_factorial *= i
        new_dictionary[i] = current_factorial
    return new_dictionary
 
if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])

# Histogram
def histogram(word: str):
    new_dictionary = {}
    for letter in word:
        if letter not in new_dictionary:
            new_dictionary[letter] = 0
        new_dictionary[letter] += 1
    for letter in new_dictionary:
        stars = "*" * new_dictionary[letter]
        print(f"{letter} {stars}")
        
    return new_dictionary
if __name__ == "__main__":
    d = histogram("histogram")

# Phone book, version 1
application = {}
while True:
    command = input("command (1 search, 2 add, 3 quit): ")
    if command == "3":
        print ("quitting...")
        break
    elif command == "2":
        name = input("name:")
        number = input("number:")
        application[name] = number
        print("ok!")
    elif command == "1":
        name = input("name:")
        if name in application:
            print(application[name])
        else:
            print("no number")
# Phone book, version 2
application = {}
while True:
    command = input("command (1 search, 2 add, 3 quit): ")
    if command == "3":
        print ("quitting...")
        break
    elif command == "2":
        name = input("name:")
        number = input("number:")
        if name not in application:
            application[name] = []
        application[name].append(number)
    
       
        print("ok!")
    elif command == "1":
        name = input("name:")
        if name in application:
            for number in application[name]:
                print(number)
        else:
            print("no number")
# Invert a dictionary
def invert(dictionary: dict):
    new_dictionary = {}
    for key in dictionary:
        value = dictionary[key]
        new_dictionary[value] = key
    dictionary.clear()
    for key in new_dictionary:
        value = new_dictionary[key]
        dictionary[key] = value
 
 
if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)

# Numbers spelled out
def dict_of_numbers():
    base = {
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
        6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
        11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
        15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"
    }
    
    tens = {
        2: "twenty", 3: "thirty", 4: "forty", 5: "fifty",
        6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"
    }
    
    numbers = {}
    
    for i in range(100):
        if i < 20:
            numbers[i] = base[i]
        else:
            ten_digit = i // 10  
            unit_digit = i % 10  
            
            if unit_digit == 0:
                numbers[i] = tens[ten_digit]
            else:
                numbers[i] = f"{tens[ten_digit]}-{base[unit_digit]}"
                
    return numbers
 
if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])

# Movie database
def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    movie = {
        "name": name,
        "director": director,
        "year": year,
        "runtime": runtime
    }
    database.append(movie)
 
if __name__ == "__main__":
    database = []
    add_movie(database, "Gone with the Python", "Victor Pything", 2017, 116)
    add_movie(database, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
    print(database)

# Find movies
def find_movies(database: list, search_term: str):
    found_movies = []
    search_term_lower = search_term.lower()
    
    for movie in database:
        name_lower = movie["name"].lower()
        director_lower = movie["director"].lower()
        
        if search_term_lower in name_lower or search_term_lower in director_lower:
            found_movies.append(movie)
    
    return found_movies
 
if __name__ == "__main__":
    database = [{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116},
    {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94},
    {"name": "Dawn of the Dead Programmers", "director": "M. Night Python", "year": 2011, "runtime": 101}]
 
    my_movies = find_movies(database, "python")
    print(my_movies)