#!/usr/bin/python3

"""
import sys module
"""
import sys

"""
This module provides an NQueens class
"""


class NQueens:
    """Class for solving the N Queens problem."""

    def __init__(self, n):
        """Initialize the NQueens object.

        Args:
            n (int): The size of the chessboard and the number of queens.
        """
        self.n = n
        self.board = [[0] * n for _ in range(n)]
        self.solutions = []

    def solve(self):
        """Solve the N Queens problem and print all solutions."""
        self.place_queen(0)
        self.print_solutions()

    def place_queen(self, row):
        """Place a queen in the given row.

        Args:
            row (int): The row to place the queen in.
        """
        if row == self.n:
            self.add_solution()
            return

        for col in range(self.n):
            if self.is_safe(row, col):
                self.board[row][col] = 1
                self.place_queen(row + 1)
                self.board[row][col] = 0

    def is_safe(self, row, col):
        """Check if it is safe to place a queen at the given position.

        Args:
            row (int): The row of the position.
            col (int): The column of the position.

        Returns:
            bool: True if it is safe to place a queen, False otherwise.
        """
        for i in range(row):
            if self.board[i][col] == 1:
                return False

        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if self.board[i][j] == 1:
                return False
            i -= 1
            j -= 1

        i = row - 1
        j = col + 1
        while i >= 0 and j < self.n:
            if self.board[i][j] == 1:
                return False
            i -= 1
            j += 1

        return True

    def add_solution(self):
        """Add the current board configuration as a solution."""
        solution = []
        for row in self.board:
            queen_col = row.index(1)
            solution.append([row.index(1), queen_col])
        self.solutions.append(solution)

    def print_solutions(self):
        """Print all solutions."""
        for solution in self.solutions:
            print(solution)


def main():
    """Main entry point of the program."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    queens = NQueens(n)
    queens.solve()


if __name__ == "__main__":
    main()
