# Star-studded
name = input("Please type in a string: ")
 
for character in name:
    print(character)
    print("*")

# From negative to positive
number = int(input("Please type in a positive integer: "))
start = -number
 
for i in range(start, number+1):
    if i != 0:
        print(i)
 
 # List of stars
def list_of_stars(my_list: list):
    star = "*"
    for i in my_list:
        print(star * i)
if __name__ == "__main__":
    my_list = [5, 2, 8, 4, 5]
    list_of_stars(my_list)

# Anagrams
def anagrams(string1: list, string2: list):
    if sorted(string1) == sorted(string2):
        return True
    else:        return False
if __name__ == "__main__":
    string1 = "mate"
    string2 = "tame"
    print(anagrams(string1, string2))

# Palindromes
def palindromes(word: str):
    return word == word[::-1]
 
while True:
    user_input = input("Please type in a palindrome: ")
    
    if palindromes(user_input):
        print(f"{user_input} is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")

# The sum of positive numbers
def sum_of_positives(my_list: list):
    list_sum = 0
    for i in my_list:
        if i >= 0:
            list_sum +=i
 
    return  list_sum
if __name__ == "__main__":
    my_list = [1, -2, 3, -4, 5]
    result = sum_of_positives(my_list)
    print("The result is", result)

# Even numbers
def even_numbers(my_list: list):
    new_list = []
    for i in my_list:
        if i%2 ==0:
            new_list.append(i)
    return new_list
 
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    new_list = even_numbers(my_list)
    print("original", my_list)
    print("new", new_list)

# The sum of lists
def list_sum(list1:list, list2:list):
    new_list = []
    for i in range(len(list1)):
        new_list.append(list1[i] + list2[i])
    return new_list
 
if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b)) # [8, 10, 12]

# Distinct numbers
def distinct_numbers(my_list:list):
    unique_list=[]
    for i in my_list:
        if i not in unique_list:
            unique_list.append(i)
 
    return sorted(unique_list)
 
if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list))

# The length of the longest in the list
def  length_of_longest(my_list):
    longest = 0
    for i in my_list:
        if len(i)>longest:
            longest = len(i)
            
    return longest
 
if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = length_of_longest(my_list)
    print(result)
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = length_of_longest(my_list)
    print(result)

# The shortest in the list
def shortest(my_list):
    shorter = my_list[0]
    
    for i in my_list:
        if len(i) < len(shorter):
            shorter = i 
    return shorter
 
 
if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = shortest(my_list)
    print(result)
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = shortest(my_list)
    print(result)

# All the longest in the list
def all_the_longest(my_list):
    if not my_list:
        return []
 
    max_len = 0
    for i in my_list:
        if len(i) > max_len:
            max_len = len(i)
 
 
    result = []
    for i in my_list:
        if len(i) == max_len:
            result.append(i)
    return result
 
if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = all_the_longest(my_list)
    print(result)
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = all_the_longest(my_list)
    print(result) 