#!/usr/bin/python3
import sys


def nqueens(n: int) -> List[List[str]]:
    """
    Solve the N-queens problem, returning all possible solutions.

    Args:
        n: The size of the chessboard.

    Returns:
        A list of all possible solutions to the N-queens problem.
    """

    def place_queen(row: int, col: int) -> List[List[str]]:
        """
        Place a queen on the board and return all possible solutions.

        Args:
            row: The row to place the queen on.
            col: The column to place the queen on.

        Returns:
            A list of all possible solutions to the N-queens problem.
        """

        # Check if the queen is attacking any other queens on the board.
        for i in range(row):
            if board[i][col] or board[row][i] or abs(row - i) == abs(col - i):
                return []

        # Place the queen on the board.
        board[row][col] = "Q"

        # If we have placed all of the queens, return the board.
        if row == n - 1:
            return [board]

        # Otherwise, recursively place the next queen.
        solutions = []
        for new_col in range(n):
            solutions += place_queen(row + 1, new_col)

        # Return the solutions.
        return solutions

    # Initialize the board.
    board = [[None for _ in range(n)] for _ in range(n)]

    # Find all possible solutions.
    solutions = []
    for col in range(n):
        solutions += place_queen(0, col)

    # Return the solutions.
    return solutions


if __name__ == "__main__":
    # Get the number of queens from the user.
    n = int(sys.argv[1])

    # Solve the N-queens problem.
    solutions = nqueens(n)

    # Print the solutions.
    for solution in solutions:
        for row in solution:
            print("".join(row))
        print()
