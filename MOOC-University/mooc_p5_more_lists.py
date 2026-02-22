# The longest string
def longest(strings: list):
    new_list = []
    for i in strings:
        if len(i) > len(new_list):
            new_list = i
    return new_list
 
 
if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))

# Number of matching elements
def count_matching_elements(my_matrix: list, element: int):
    count = 0
    for i in my_matrix:
        for j in i:
            if j == element:
                count += 1
    return count
 
 
if __name__ == "__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(count_matching_elements(m, 1))

# Go
def who_won(game_board: list):
    empties = 0
    player1=1
    player2=2
    list_player1 = []
    list_player2 = []
    for i in game_board:
        for j in i:
            if j == 0:
                empties += 1
            elif j == player1:
                list_player1.append(j)
            elif j == player2:
                list_player2.append(j)
 
    if len(list_player1) > len(list_player2):
        return 1
    elif len(list_player2) > len(list_player1):
        return 2
    else:
        return 0
 
if __name__ == "__main__":
    board = [[1, 2, 0], [2, 1, 0], [2, 0, 1]]
    print(who_won(board))

# Sudoku: check row
def row_correct(sudoku: list, row_no: int):
    numbers_seen = []
    for row in sudoku[row_no]:
       if row > 0:
           if row in numbers_seen:
               return False
           numbers_seen.append(row)
    return True
 
 
 
 
if __name__ == "__main__":
    sudoku = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
     [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]
 
    print(row_correct(sudoku, 0))
    print(row_correct(sudoku, 1))

# Sudoku: check column
def column_correct(sudoku: list, column_no: int):
    numbers_seen = []
    for row in sudoku:
        if row[column_no] > 0:
            if row[column_no] in numbers_seen:
                return False
            numbers_seen.append(row[column_no])
    return True
 
 
if __name__ == "__main__":
    sudoku = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]
 
    print(column_correct(sudoku, 0))
    print(column_correct(sudoku, 1))

# Sudoku: check block
def block_correct(sudoku: list, row_no: int, column_no: int):
    numbers_seen = []
    for row in range(row_no, row_no+3):
        for column in range(column_no, column_no+3):
            if sudoku[row][column] > 0:
                if sudoku[row][column] in numbers_seen:
                    return False
                numbers_seen.append(sudoku[row][column])
    return True
 
 
if __name__ == "__main__":
    sudoku = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]
 
    print(block_correct(sudoku, 0, 0))
    print(block_correct(sudoku, 1, 2))

# Sudoku: check grid
def row_correct(sudoku: list, row_no: int):
    numbers = []
    for number in sudoku[row_no]:
        if number > 0 and number in numbers:
            return False
        numbers.append(number)
 
    return True
 
def column_correct(sudoku: list, column_no: int):
    numbers = []
    for row in sudoku:
        number = row[column_no]
        if number > 0 and number in numbers:
            return False
        numbers.append(number)
 
    return True
 
def block_correct(sudoku: list, row_no: int, column_no: int):
    numbers = []
    for r in range(row_no, row_no+3):
        for s in range(column_no, column_no+3):
            number = sudoku[r][s]
            if number > 0 and number in numbers:
                return False
            numbers.append(number)
 
    return True
 
def sudoku_grid_correct(sudoku: list):
    for row in range(0,9):
        if not row_correct(sudoku, row):
            return False
 
    for column in range(0,9):
        if not column_correct(sudoku, column):
            return False
 
    for row in range(0,9,3):
        for column in range(0,9,3):
            if not block_correct(sudoku, row, column):
                return False
 
    return True