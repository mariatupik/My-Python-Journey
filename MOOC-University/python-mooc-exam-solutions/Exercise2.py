def copy(matrix: list):
    new_matrix = []
    for row in matrix:
        new_matrix.append(row[:])
    return new_matrix

def flip(matrix: list):
    for row in matrix:
        row[0], row[1] = row[1], row[0]
   
def flip_and_copy(matrix: list):
    new_matrix = copy(matrix)
    flip(new_matrix)
    return new_matrix

if __name__ == "__main__":
    matrix = [
        ["Donald Duck", 80],
        ["Mickey Mouse", 60],
        ["Moomintroll", 120],
        ["Snoopy", 40],
        ["Goofy Goof", 100]
    ]

    flipped_copy = flip_and_copy(matrix)
    copy_of_original = copy(matrix)
    flip(matrix)

    print("Copy:")
    for row in copy_of_original:
        print(row)

    print("\nFlipped:")
    for row in matrix:
        print(row)