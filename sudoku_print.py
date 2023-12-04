from sudoku_solution import SudokuSolution
from sudoku_validate import SudokuValidate

class SudokuPrint:
    @staticmethod
    def print_grid(grid):
        """
            print solved grid as a single line, example: 
            [1,2,3]
            [4,5,6]
            To 1 2 3 4 5 6
        """
        for row in grid:
            print(" ".join(map(str, row)), end=" ")

    def complete_sudoku(grid):
        # Try to solve sudoku, if the sudoku grid is impossible to solve, so print "No solution exists"
        if SudokuSolution.solve_sudoku(grid):
            if SudokuValidate.verify_repeated_numbers(grid):
                return
            SudokuPrint.print_grid(grid)
        else: print("No solution exists")