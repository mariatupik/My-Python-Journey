# Change the value of an item
list = [1, 2, 3, 4, 5]
while True:
    index = int(input("Index:"))
    if index == -1:
        break
    new_velue = int(input("New value:"))
    if index == -1:
        break
    else:
        list[index] =  new_velue
        print(list)

# Add items to a list
my_list = []
number = int(input("How many items: "))
for i in range(number):
    list1 = int(input(f"Item {i+1}: "))
    my_list.append(list1)
print(my_list)

# Addition and removal
my_list = []
 
while True:
    print(f"The list is now {my_list}")
    
    choice = input("a(d)d, (r)emove or e(x)it: ")
    
    if choice == "x":
        break
    
    elif choice == "d":
        item = len(my_list) + 1
        my_list.append(item)
        
    elif choice == "r":
        if len(my_list) > 0:
            my_list.pop()
 
print("Bye!")
 
 # Same word twice
my_list = []
 
while True:
    word = input("Word: ") 
    if word in my_list:
        print(f"You typed in {len(my_list)} different words")
        break
    my_list.append(word)

# List twice

my_list = []
while True:
    item = int(input("New item:"))
    if item == 0:
        break
    else:
        my_list.append(item)
        print(f"The list now: {my_list}")
        order = sorted(my_list)
        print(f"The list in order: {order}")
    
print("Bye!")

# The length of a list
def length(list1):
    return len(list1)
 
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    result = length(my_list)
    print("The length is", result)

# Arithmetic mean
def mean(my_list: list):
       list_centre = sum(my_list) / len(my_list)
       return list_centre
 
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    result = mean(my_list)

#The range of a list
def range_of_list (my_list: list):
    greatest = max(my_list)
    smallest = min(my_list)
    difference = greatest - smallest
    return difference
 
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    result = range_of_list(my_list)
    print("The range of the list is", result)




