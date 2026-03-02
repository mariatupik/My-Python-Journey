# Reading input
def read_input(nput_str, x, y):
     while True:
        try:
            input_str = input("Please type in a number: ")
            number = int(input_str)
            if x <= number <= y:
                return number
        except ValueError:
            pass
        print(f"You must type in an integer between {x} and {y}")
 
if __name__ == "__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)
 
# Parameter validation
def new_person(name: str, age: int):
    if not name or len(name) > 40 or len(name.split()) < 2:
        raise ValueError("name is Error")
    if age < 0 or age > 150:
        raise ValueError("age is Error")
    return (name, age)

# Incorrect lottery numbers
def filter_incorrect():
    open("correct_numbers.csv", "w").close()
    with open("lottery_numbers.csv") as new_file:
        for line in new_file:
            clean_line = line.replace("\n", "")
            parts = line.split(";")
            week = parts[0]
            numbers_str = parts[1].split(",")
            try:
                week_parts = parts[0].split()
                int(week_parts[1])
                if len(numbers_str) != 7:
                    raise ValueError
                numbers = []
                for n in numbers_str:
                    num = int(n)
                    if num < 1 or num > 39:
                        raise ValueError
                    numbers.append(num)
                if len(set(numbers)) != 7:
                    raise ValueError
                with open("correct_numbers.csv", "a") as file2:
                    file2.write(clean_line + "\n")
            except:
                continue