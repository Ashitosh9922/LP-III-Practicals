# N-Queens Problem using Backtracking
# -----------------------------------
# The goal is to place N queens on an N×N chessboard so that
# no two queens attack each other in the same row, column, or diagonal.

def print_board(board, n):
    """Print the chessboard"""
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()
    print()


def is_safe(board, row, col, n):
    """Check if a queen can be safely placed"""

    # Check column above
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_nqueens(board, row, n):
    """Recursive function to solve N-Queens using backtracking"""
    if row == n:
        print("Solution exists for the given position of the first queen:\n")
        print_board(board, n)
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1  # Place queen
            if solve_nqueens(board, row + 1, n):
                return True
            board[row][col] = 0  # Backtrack (remove queen)

    return False


# Step 1: Input board size
n = int(input("Enter the number of queens (n): "))

# Step 2: Create an empty N×N board
board = []
for i in range(n):
    row = [0] * n
    board.append(row)

# Step 3: Place the first queen manually
first_row = int(input("Enter row position for first queen (0-indexed): "))
first_col = int(input("Enter column position for first queen (0-indexed): "))
board[first_row][first_col] = 1

# Step 4: Try to solve
if not solve_nqueens(board, first_row + 1, n):
    print("No solution exists for the given position of the first queen.")

"""
SAMPLE OUTPUT 1 (Solution Exists)
----------------------------------
Enter the number of queens (n): 4
Enter row position for first queen (0-indexed): 0
Enter column position for first queen (0-indexed): 1

Solution exists for the given position of the first queen:

0 1 0 0
0 0 0 1
1 0 0 0
0 0 1 0


SAMPLE OUTPUT 2 (No Solution Exists)
------------------------------------
Enter the number of queens (n): 4
Enter row position for first queen (0-indexed): 0
Enter column position for first queen (0-indexed): 0

No solution exists for the given position of the first queen.


THEORY / APPROACH
-----------------
Problem:
Place N queens on an N×N chessboard so that no two queens attack each other.

Rules:
1. Only one queen per row.
2. Queens cannot be in the same column or diagonal.

Steps:
1. Start with the first queen placed by the user.
2. Move to the next row.
3. Try placing a queen in each column.
4. If a safe position is found, place it and move to the next row.
5. If no safe position is found, backtrack (remove previous queen and try a new spot).
6. Continue until all queens are placed or no solution exists.

Approach Used:
Backtracking – explore, check, and undo steps when conflicts occur.

Time Complexity: O(N!)
Space Complexity: O(N²)

Real-life Analogy:
Like assigning N people to N rooms so that no two people disturb each other.
If a conflict occurs, go back and change earlier assignments until all fit peacefully.
"""
