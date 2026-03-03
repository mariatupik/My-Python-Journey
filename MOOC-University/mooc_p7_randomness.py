# Lottery numbers
from random import sample
 
def lottery_numbers(amount: int, lower: int, upper: int):
    number_pool = list(range(lower, upper+1))
    weekly_draw = sample(number_pool, amount)
    return sorted(weekly_draw)
 
if __name__ == "__main__":
    for number in lottery_numbers(7, 1, 40):
        print(number)

# Password generator, part 1
import string
from random import sample
 
def generate_password (amount: int):
    chatacter_pool = list(string.ascii_lowercase)
    password = sample(chatacter_pool, amount)
    return "".join(password)
 
if __name__ == "__main__":
    for i in range(10):
        print(generate_password(8))

# Password generator, part 2
import string
import random
 
def generate_strong_password(amount: int, boolean1: bool, boolean2: bool):
    password = [random.choice(string.ascii_lowercase)]
    pool = list(string.ascii_lowercase)
    
    if boolean1:
        digit = random.choice(string.digits)
        password.append(digit)
        pool += list(string.digits)
        
    if boolean2:
        special = random.choice("!?=+-()#")
        password.append(special)
        pool += list("!?=+-()#")
    
    remaining_amount = amount - len(password)
    password += random.sample(pool, remaining_amount)
    
    random.shuffle(password)
    
    return "".join(password)
 
if __name__ == "__main__":
    for i in range(10):
        print(generate_strong_password(8, True, True))

# Dice roller
import string
import random
def roll(die: str):
    dice = {"A": [3, 3, 3, 3, 3, 6], "B": [2, 2, 2, 5, 5, 5],"C": [1, 4, 4, 4, 4, 4] }
    return random.choice(dice[die])
def play(die1: str, die2: str, times: int):
    wins1 = 0
    wins2 = 0
    draws = 0
    for i in range(times):
        res1 = roll(die1)
        res2 = roll(die2)
        
        if res1 > res2:
            wins1 += 1
        elif res2 > res1:
            wins2 = wins2 + 1
        else:
            draws += 1
            
    return (wins1, wins2, draws)
 
 
if __name__ == "__main__":
    for i in range(20):
        print(roll("A"), " ", end="")
    print()
    for i in range(20):
        print(roll("B"), " ", end="")
    
    print()
    for i in range(20):
        print(roll("C"), " ", end="")
    result = play("A", "C", 1000)
    print(result)
    result = play("B", "B", 1000)
    print(result)

# Random words
from random import sample
 
def words(n: int, beginning: str):
    word_list = []
    length = len(beginning)
    with open("words.txt") as file:
 
        for line in file:
            word = line.strip()
            if word[:length] == beginning:
                word_list.append(word)
 
    if len(word_list) < n:
        raise ValueError
    result = sample(word_list, n)
    
    return result
 
if __name__ == "__main__":
    word_list = words(3, "ca")
    for word in word_list:
        print(word)
