from sudoku_solution import SudokuSolution
from sudoku_validate import SudokuValidate

class SudokuPrint:
    @staticmethod
    def print_grid(grid):
        for row in grid:
            print(" ".join(map(str, row)), end=" ")

    def complete_sudoku(grid):
        if SudokuSolution.solve_sudoku(grid):
            if SudokuValidate.verify_repeated_numbers(grid):
                return
            SudokuPrint.print_grid(grid)
        else: print("No solution exists")