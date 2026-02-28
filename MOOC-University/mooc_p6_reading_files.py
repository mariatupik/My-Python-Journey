# Largest number
def largest():
    with open("numbers.txt") as new_file:
        number = []
    
        for line in new_file:
            line = int(line)
            number.append(line)
 
    return max(number)
if __name__ == "__main__":    
    print(largest())
 
# Fruit market

def read_fruits():
    with open("fruits.csv") as new_file:
        market = {}
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            name = parts[0]
            prices = parts[1]
            market[name]=float(prices)
        return market
if __name__ == "__main__":    
    print(read_fruits())

# Matrix
def matrix_sum():
    with open("matrix.txt") as new_file:
        total_sum = 0
        for line in new_file:
            line = line.strip()
            parts = line.split(",")
            for item in parts:
                item = float(item)
                total_sum+=item
        return int(total_sum)
    
def matrix_max():
    with open("matrix.txt") as new_file:
        number = []
        for line in new_file:
            line = line.strip()
            parts = line.split(",")
            for item in parts:
                item = int(item)
                number.append(item)
    return max(number)
 
def row_sums():
    with open("matrix.txt") as new_file:
        parts_sum=[]
        for line in new_file:
            line = line.strip()
            parts = line.split(",")
            row_sum = 0
            for item in parts:
                row_sum += float(item)
            parts_sum.append(row_sum)    
    return parts_sum
 
 
if __name__ == "__main__":    
    print(matrix_sum())
    print(matrix_max())
    print(row_sums())

# Course grading
student_inf=input("Student information:")
exercises_compl=input("Exercises completed:")
exam_points=input("Exam points:")
 
students = {}
 
with open(student_inf) as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        parts = line.split(';')
        if parts[0] == "id":
            continue
        students[parts[0]] = parts[1] + " " + parts[2]
 
exercises = {}
 
with open(exercises_compl) as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] == "id":
            continue
        total = 0
        for score in parts[1:]:
            total += int(score)
        exercises[parts[0]] = total
 
grading = {}
 
with open(exam_points) as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] == "id":
            continue
        total = 0
        for grade in parts[1:]:
            total += int(grade)
        grading[parts[0]] = total
 
print(f"{'name':30}{'exec_nbr':10}{'exec_pts.':10}{'exm_pts.':10}{'tot_pts.':10}{'grade':10}")
for id, name in students.items():
    exercise = exercises[id]
    grad=grading[id]
    exercise_points = exercise // 4
    total=grading[id]+exercise_points
    if 0 <= total <= 14:
        grade=0
    elif 15 <= total <= 17:
        grade=1
    elif 18 <= total <= 20:
        grade=2
    elif 21 <= total <= 23:
        grade=3
    elif 24 <= total <= 27:
        grade=4
    elif 28 <= total:
        grade=5
 
    print(f"{name:30}{exercise:<10}{exercise_points:<10}{grad:<10}{total:<10}{grade:<10}")
 
# Spell checker
wordlist = []
with open("wordlist.txt") as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        wordlist.append(line)
 
 
text = input("Write text: ")
words = text.split()
 
for word in words:
    clean_word = word.strip(".,!?;:").lower()
    if clean_word in wordlist:
        print(word, end=" ")
    else:
        print(f"*{word}*", end=" ")

# Recipe search

def search_by_name(filename: str, word: str):
    with open(filename) as f:
        content = f.read()
        recipe_blocks = content.split("\n\n") 
    found = []
    for block in recipe_blocks:
        lines = block.split("\n")
        recipe_name = lines[0]
        if word.lower() in recipe_name.lower():
            found.append(recipe_name)
            
    return found
 
def search_by_time(filename: str, prep_time: int):
    found_recipes = []
    with open(filename) as f:
        content = f.read().strip()
        recipes_list = content.split("\n\n")
    for recipe in recipes_list:
        lines = recipe.split("\n")
        name = lines[0]
        time = int(lines[1]) 
        
        if time <= prep_time:
            found_recipes.append(f"{name}, preparation time {time} min")
            
    return found_recipes
 
def search_by_ingredient(filename: str, ingredient: str):
    found_recipes = []
    with open(filename) as f:
        content = f.read().strip()
        recipes_list = content.split("\n\n")
    for recipe in recipes_list:
        lines = recipe.split("\n")
        name = lines[0]
        time = int(lines[1])
        ingredients = "\n".join(lines[2:])
            
        if ingredient.lower() in ingredients.lower():
            found_recipes.append(f"{name}, preparation time {time} min")
                
    return found_recipes
 
if __name__ == "__main__":
    found_recipes = search_by_name("recipes1.txt", "cake")
    for recipe in found_recipes:
        print(recipe)
 
    found_recipes = search_by_time("recipes1.txt", 20)                             
    for recipe in found_recipes:
        print(recipe)
    found_recipes = search_by_ingredient("recipes1.txt", "eggs")
 
    for recipe in found_recipes:
        print(recipe)

# City bikes

import math
 
def get_station_data(filename: str):
    stations = {}
    with open(filename) as file:
        for line in file:
            parts = line.strip().split(';')
            if parts[0] == "Longitude":
                continue
            stations[parts[3]] = (float(parts[0]), float(parts[1]))
    return stations
 
def distance(stations: dict, station1: str, station2: str):
    long1, lat1 = stations[station1]
    long2, lat2 = stations[station2]
    x_km = (long1 - long2) * 55.26
    y_km = (lat1 - lat2) * 111.2
 
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km
 
def greatest_distance(stations: dict):
    max_dist = -1.0
    st1 = ""
    st2 = ""
    
    station_names = list(stations.keys())
    
    for i in range(len(station_names)):
        for j in range(i + 1, len(station_names)):
            name1 = station_names[i]
            name2 = station_names[j]
            
            current_dist = distance(stations, name1, name2)
            
            if current_dist > max_dist:
                max_dist = current_dist
                st1 = name1
                st2 = name2
                
    return st1, st2, max_dist
 
if __name__ == "__main__":
    stations = get_station_data('stations1.csv')
    s1, s2, dist = greatest_distance(stations)
    print(f"{s1} {s2} {dist}")
