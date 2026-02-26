# Items multiplied by two
def  double_items(numbers: list):
    new_list = []
    for number in numbers:
        new_list.append(number * 2)
    return new_list
 
 
if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)

# Remove the smallest
def remove_smallest(numbers: list):
    i = min(numbers)
    numbers.remove(i)
 
if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)

# Sudoku: print out the grid and add a number
def print_sudoku(sudoku: list):
    for i in range(9):
        if i > 0 and i % 3 == 0:
            print()
            
        for j in range(9):
            if j > 0 and j % 3 == 0:
                print(" ", end="")
            char = sudoku[i][j] if sudoku[i][j] > 0 else "_"
            
            if j == 0:
                print(f"{char}", end="")
            else:
                
                print(f" {char}", end="")
        
        print()
 
def add_number(sudoku: list, row_no: int, column_no: int, number: int):
    sudoku[row_no][column_no] = number
 
if __name__ == "__main__":
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
 
    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)

# Sudoku: add number to a copy of the grid
def print_sudoku(sudoku: list):
    for i in range(9):
        if i > 0 and i % 3 == 0:
            print()
            
        for j in range(9):
            if j > 0 and j % 3 == 0:
                print(" ", end="")
            char = sudoku[i][j] if sudoku[i][j] > 0 else "_"
            
            if j == 0:
                print(f"{char}", end="")
            else:
                
                print(f" {char}", end="")
        
        print()
def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    copy = [row[:] for row in sudoku]
    copy[row_no][column_no] = number
    return copy
 
if __name__ == "__main__":
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
 
    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)

# Tic-Tac-Toe
def play_turn(game_board: list, x: int, y: int, piece: str):
    player1 = "X"
    player2 = "O"
    if 0 <= x <= 2 and 0 <= y <= 2 and game_board[y][x] == "":
        game_board[y][x] = piece
        return True
    else:
        return False
    
if __name__ == "__main__":
    game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(play_turn(game_board, 2, 0, "X"))
    print(game_board)

# Transpose a matrix
def transpose(matrix: list):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
 
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    transpose(matrix)
    print(matrix)