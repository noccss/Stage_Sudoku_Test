from sudoku_validate import SudokuValidate

class SudokuSolution:
    @staticmethod
    def locate_blank_house(grid):
        # Executes a loop to identify all blank spaces (0). Returns None if no more blank fields are found.
        for row in range(len(grid)):
            for column in range(len(grid)):
                if grid[row][column] == 0:
                    return row, column
        return None, None

    @staticmethod
    def solve_sudoku(grid):
        row, column = SudokuSolution.locate_blank_house(grid)
        # If row and column is None, so Sudoku is solved. Else validate movimento by num
        if row is None and column is None:
            return True
        for num in range(1, len(grid) + 1):
            if not SudokuValidate.validate_upright_horizontal_moviment(grid, row, column, num) and \
                    SudokuValidate.validate_subgrid_moviment(grid, row, column, num):
                grid[row][column] = num
                if SudokuSolution.solve_sudoku(grid):
                    return True
                grid[row][column] = 0
