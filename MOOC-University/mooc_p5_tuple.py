# Create a tuple
def create_tuple(x: int, y: int, z: int):
    new_tuple=()
    my_list=[x,y,z]
    new_tuple=(min(my_list), max(my_list), sum(my_list))
    return new_tuple
if __name__ == "__main__":
    print(create_tuple(5, 3, -1))

# The oldest person
def oldest_person(people: list):
    oldest = people[0]
    for person in people:
        if person[1] < oldest[1]:
            oldest = person
    return oldest[0]
 
if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]
 
    print(oldest_person(people))

# Older people
def older_people(people: list, year: int):
    oldest = people[0]
    before = []
    for person in people:
        if person[1] < year:
            oldest = person[0]
            before.append(person[0])
    return before
 
if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]
 
    older = older_people(people, 1979)
    print(older)

# Student database
def add_student(students: dict, name: str):
    students[name] = []
 
def print_student(students: dict, name: str):
    if name not in students:
        print(f"{name}: no such person in the database")
        return
 
    print(name + ":")
    courses = students[name]
    
    if not courses:
        print(" no completed courses")
    else:
        print(f" {len(courses)} completed courses:")
        
        total_grade = 0
        for course in courses:
            course_name, grade = course
            print(f"  {course_name} {grade}")
            total_grade += grade  
        average = total_grade / len(courses)
        print(f" average grade {average}")
 
def add_course(students: dict, name: str, course_info: tuple):
    course_name = course_info[0]
    grade = course_info[1]
    if grade == 0:
        return
    if name not in students:
        return
    found_index = -1
    for i in range(len(students[name])):
        if students[name][i][0] == course_name:
            found_index = i
            break
 
    if found_index == -1:
        students[name].append(course_info)
    else:
        old_grade = students[name][found_index][1]
        if grade > old_grade:
            students[name][found_index] = course_info
def summary(students: dict):
    print(f"students {len(students)}")
    most_courses_count = 0
    most_courses_student = ""
    best_avg = 0
    best_avg_student = ""
    for name, courses in students.items():
        if len(courses) > most_courses_count:
            most_courses_count = len(courses)
            most_courses_student = name
        if courses:
            avg = sum(c[1] for c in courses) / len(courses)
            if avg > best_avg:
                best_avg = avg
                best_avg_student = name
                
    print(f"most courses completed {most_courses_count} {most_courses_student}")
    print(f"best average grade {best_avg:.1f} {best_avg_student}")
    
 
if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    print_student(students, "Peter")
    print_student(students, "Eliza")
    print_student(students, "Jack")
    students = {}
    add_student(students, "Peter")
    add_course(students, "Peter", ("Introduction to Programming", 3))
    add_course(students, "Peter", ("Advanced Course in Programming", 2))
    print_student(students, "Peter")
    students = {}
    add_student(students, "Peter")
    add_course(students, "Peter", ("Introduction to Programming", 3))
    add_course(students, "Peter", ("Advanced Course in Programming", 2))
    add_course(students, "Peter", ("Data Structures and Algorithms", 0))
    add_course(students, "Peter", ("Introduction to Programming", 2))
    print_student(students, "Peter")
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)

# A square of letters
n = int(input("Layers: "))
size = 2 * n - 1
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
 
for i in range(size):
    line = ""
    for j in range(size):
        dist_top = i
        dist_bottom = size - 1 - i
        dist_left = j
        dist_right = size - 1 - j
        layer_index = min(dist_top, dist_bottom, dist_left, dist_right)
        letter = alphabet[n - 1 - layer_index]
        line += letter
        
    print(line)