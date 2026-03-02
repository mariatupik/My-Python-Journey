# Inscription
name = input("Whom should I sign this to:")
file = input("Where shall I save it:")
with open(file, "w") as my_file:
    my_file.write(f"Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")

# Diary
while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    numb_function = int(input("Function: "))
    if numb_function == 0:
        print("Bye now!")
        break
    elif numb_function == 1:
        add = input("Diary entry: ")
        with open("diary.txt", "a") as my_file:
            my_file.write(f"{add}\n")
        print("Diary saved")
    elif numb_function == 2:
        print("Entries:")
        with open("diary.txt") as new_file:
            contents = new_file.read()
            print(contents)

# Filtering the contents of a file
def filter_solutions():
    correct_list = []
    incorrect_list = []
    with open("solutions.csv") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            name_of_student = parts[0]
            problem = parts[1]
            result = parts[2]
            if "+" in problem:
                parts_problem = problem.split("+")
                calculated = int(parts_problem[0]) + int(parts_problem[1])
            elif "-" in problem:
                parts_problem = problem.split("-")
                calculated = int(parts_problem[0]) - int(parts_problem[1])           
            new_string = f"{name_of_student};{problem};{result}\n"
            if calculated == int(result):
                correct_list.append(new_string)
            if calculated != int(result):
                incorrect_list.append(new_string)
    with open("correct.csv", "w") as f_correct:
        for line in correct_list:
            f_correct.write(line)
            
    with open("incorrect.csv", "w") as f_incorrect:
        for line in incorrect_list:
            f_incorrect.write(line)
    
if __name__ == "__main__":    
    filter_solutions()

# Store personal data
def store_personal_data(person: tuple):
    name, age, height = person
    line = f"{name};{age};{height}\n"
 
    with open("people.csv", "a") as my_file:
        my_file.write(f"{line}\n")

# Course grading, part 4

def read_weekly_points(filename):
    weekly_points = {}
    with open(filename) as my_file:
        for line in my_file:
            parts = line.strip().split(";")
            if parts[0] == "id":
                continue
            point_list = []
            for points in parts[1:]:
                point_list.append(int(points))
            weekly_points[parts[0]] = point_list
    return weekly_points
 
def grade(points):
    if points < 15:
        return 0
    elif points < 18:
        return 1
    elif points < 21:
        return 2
    elif points < 24:
        return 3
    elif points < 28:
        return 4
    else:
        return 5
 
student_file = input("Student information: ")
exercise_file = input("Exercises completed: ")
exam_file = input("Exam points: ")
course_file = input("Course information: ")
 
students = {}
with open(student_file) as f:
    for line in f:
        parts = line.strip().split(';')
        if parts[0] == "id":
            continue
        students[parts[0]] = f"{parts[1]} {parts[2]}"
 
exercises = read_weekly_points(exercise_file)
exams = read_weekly_points(exam_file)
 
with open(course_file) as f:
    lines = f.readlines()
    c_name = lines[0].split(":")[1].strip()
    c_credits = lines[1].split(":")[1].strip()
 
header = f"{c_name}, {c_credits} credits"
divider = "=" * len(header)
 
with open("results.txt", "w") as f_txt, open("results.csv", "w") as f_csv:
    f_txt.write(f"{header}\n")
    f_txt.write(f"{divider}\n")
    f_txt.write(f"{'name':30}{'exec_nbr':10}{'exec_pts.':10}{'exm_pts.':10}{'tot_pts.':10}{'grade':10}\n")
    
    for s_id in students:
        name = students[s_id]
        total_ex = sum(exercises[s_id])
        ex_pts = total_ex // 4
        exam_pts = sum(exams[s_id])
        total_pts = ex_pts + exam_pts
        final_grade = grade(total_pts)
        
        f_txt.write(f"{name:30}{total_ex:<10}{ex_pts:<10}{exam_pts:<10}{total_pts:<10}{final_grade:<10}\n")
        f_csv.write(f"{s_id};{name};{final_grade}\n")
 
print("Results written to files results.txt and results.csv")

# Word search
def find_words(search_term: str):
    wordlist = []
    search_list = []
    with open("words.txt") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            wordlist.append(line)
 
        for item in wordlist:
            if search_term[len(search_term)-1] == "*":
                prefix = search_term[:-1]
                if item[:len(prefix)] == prefix:
                    search_list.append(item)
            elif search_term[0] == "*":
                suffix = search_term[1:]
                if item[len(item)-len(suffix):] == suffix:
                    search_list.append(item)
            elif "." in search_term:
                if len(item) == len(search_term):
                    match = True
                    for i in range(len(search_term)):
                        if search_term[i] != "." and search_term[i] != item[i]:
                            match = False
                            break
                    if match:
                        search_list.append(item)
            else:
                if item == search_term:
                    search_list.append(item)
                
    return search_list
 
 
if __name__ == "__main__":
    print(find_words("*vokes"))
 
# Dictionary stored in a file
new_dictionary = {}
 
with open("dictionary.txt", "a") as initial_check:
    pass
 
with open("dictionary.txt", "r") as file:
    for line in file:
        line = line.replace("\n", "")
        if " - " in line:
            parts = line.split(" - ")
            finnish = parts[0]
            english = parts[1]
            if finnish not in new_dictionary:
                new_dictionary[finnish] = []
            new_dictionary[finnish].append(english)
 
while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    command = input("Function: ")
    
    if command == "3":
        print("Bye!")
        break
        
    elif command == "1":
        finnish_word = input("The word in Finnish: ")
        english_word = input("The word in English: ")
        
        if finnish_word not in new_dictionary:
            new_dictionary[finnish_word] = []
        new_dictionary[finnish_word].append(english_word)
        
        with open("dictionary.txt", "a") as my_file:
            my_file.write(f"{finnish_word} - {english_word}\n")
        print("Dictionary entry added")
        
    elif command == "2":
        term = input("Search term: ")
        results = []
        for finnish, english_list in new_dictionary.items():
            found_in_finnish = term in finnish
            found_in_english = False
            for eng in english_list:
                if term in eng:
                    found_in_english = True
            if found_in_finnish or found_in_english:
                for eng in english_list:
                    results.append(f"{finnish} - {eng}")
        
        if len(results) > 0:
            for res in results:
                print(res)