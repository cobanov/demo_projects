from collections import defaultdict


matrix = defaultdict(lambda: "_")


def update_board():
    board = f"""
 ---+---+---
| {matrix[0]}   {matrix[1]}   {matrix[2]} |
 ---+---+---
| {matrix[3]}   {matrix[4]}   {matrix[5]} |
 ---+---+---
| {matrix[6]}   {matrix[7]}   {matrix[8]} |
 ---+---+---"""
    return board


def check_available():
    available = []

    for key, value in matrix.items():
        if value == "_":
            available.append(key)

    return available


def check_table(board, matrix):

    # check columns
    for i in [0, 1, 2]:
        if matrix[i] == matrix[i+3] == matrix[i+6] != "_":
            return False

    # check rows
    for i in [0, 3, 6]:
        if matrix[i] == matrix[i+1] == matrix[i+2] != "_":
            print("Game Over")
            return False

    if matrix[0] == matrix[4] == matrix[8] != "_":
        print("Game Over")
        return False

    if (matrix[2] == matrix[4] == matrix[5] != "_"):
        print("Game Over")
        return False

    return True


def insert(available):

    if len(available) % 2 == 0:
        print("X's turn\n")
        value = 'X'

    if len(available) % 2 != 0:
        print("O's turn\n")
        value = 'O'

    print("Select an available place")
    print(available)
    selection = int(input("\nSelected: "))

    if selection in available:
        matrix[selection] = value
        print("updated")

    else:
        print("Wrong")


def main():
    Status = True
    while True:
        board = update_board()
        print(board)
        if not Status:
            break
        available = check_available()
        insert(available)
        Status = check_table(board, matrix)


if __name__ == "__main__":

    main()
