import random

def is_safe(board, row, col, n):
  
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_n_queens(n):
    def backtrack(row):
        if row == n:
            return board.copy()
        random.shuffle(columns)
        for col in columns:
            if is_safe(board, row, col, n):
                board[row] = col
                result = backtrack(row + 1)
                if result:
                    return result
        return None

    board = [-1] * n
    columns = list(range(n))
    return backtrack(0)

def print_board(solution):
    n = len(solution)
    for i in range(n):
        row = ['.'] * n
        row[solution[i]] = 'Q'
        print(' '.join(row))
    print()

n = 8  
solution = solve_n_queens(n)
if solution:
    print("Solution Found:")
    print_board(solution)
else:
    print("No solution found.")