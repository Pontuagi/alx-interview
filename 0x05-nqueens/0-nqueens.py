#!/usr/bin/python3

"""
Nqueens modules
N Queens puzzle of placing N non attacking queens on an N * n chessboard
"""

import sys


def is_safe(board, row, col, N):
    """Check if there is a queen in the same column"""
    for i in range(row):
        if board[i] == col
                or board[i] - i == col - row
                or board[i] + i == col + row:
            return False
        return True


def solve_nqueens(board, row, N):
    if row == N:
        print_solution(board, N)
        return
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col
            solve_nqueens(board, row + 1, N)


def print_solution(board, N):
    for i in range(N):
        print(board[i]], end=' ')
    print()


def main():
    # Check for the correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Get N from command line argument
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is greater or equal to 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the chessboard
    board = [-1] * N

    # Solve and print solutions
    solve_nqueens(board, 0, N)

if __name__ == "__main__":
    main()
