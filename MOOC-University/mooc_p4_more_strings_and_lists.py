# Most common character
def most_common_character(my_string: str):
    max_count = 0
    max_ch=0
    for ch in my_string:
        if my_string.count(ch) > max_count:
            max_count = my_string.count(ch)
            max_ch= ch
    return max_ch
 
if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))
 
    second_string = "exemplaryelementary"
    print(most_common_character(second_string))

# No vowels allowed
def no_vowels(my_string: str):
    vowels = "aeiou" 
    result = ""
    for ch in my_string:
        if ch not in vowels:
            result += ch
    return result
 
if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))

# No shouting allowed
def no_vowels(my_string: str):
    vowels = "aeiou" 
    result = ""
    for ch in my_string:
        if ch not in vowels:
            result += ch
    return result

if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))

# Neighbours in a list
def longest_series_of_neighbours(my_list: list):
    longest_series = 1
    current_series = 1
    for i in range(len(my_list) - 1):
        if my_list[i] == my_list[i + 1] - 1 or my_list[i] == my_list[i + 1] + 1:
            current_series += 1
        else:
            if current_series > longest_series:
                longest_series = current_series
            current_series = 1
    if current_series > longest_series:
        longest_series = current_series
    return longest_series
 
 
 
if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))

# Grade statistics

def exercises_to_points(exercises):
    exercise_points = exercises // 10
    return exercise_points
 
def calculate_grade(exam_points, exercise_points):
    if exam_points < 10:
        return 0
    total = exam_points + exercise_points
    if 0 <= total <= 14:
        return 0
    elif 15 <= total <= 17:
        return 1
    elif 18 <= total <= 20:
        return 2
    elif 21 <= total <= 23:
        return 3
    elif 24 <= total <= 27:
        return 4
    elif 28 <= total <= 30:
        return 5
    
final_points = []
grades =[]
 
all_results = []
while True:
    entry = input("Exam points and exercises completed: ")
    if entry == "": 
        break
 
    else:
 
        parts = entry.split()
        exam_points = int(parts[0])
        exercises_done = int(parts[1])
        ex_points = exercises_to_points(exercises_done)
        total = exam_points + ex_points
        current_grade = calculate_grade(exam_points, ex_points)
        final_points.append(total)
        grades.append(current_grade)
 
print("Statistics:")
average = sum(final_points) / len(final_points)
print(f"Points average: {average:.1f}")
 
passed_count = 0
for i in grades:
    if i > 0:
        passed_count += 1
pass_percentage=passed_count/(len(grades))*100
print(f"Pass percentage: {pass_percentage:.1f}")
print("Grade distribution:")
for i in range(5, -1, -1):
    count = grades.count(i)
    print(f"  {i}: {'*' * count}")