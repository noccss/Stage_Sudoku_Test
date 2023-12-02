GRID = [
    [3, 0, 6, 5, 7, 8, 4, 9, 2],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0]
]

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

class SudokuValidate:
    @staticmethod
    def verify_repeated_numbers(grid):
        def print_error(position_error, repeated_number, direction, quantity_error):
            print(False)
            print("Explanation:")
            print("No solution exists")
            print(f"There does not exist a valid Sudoku for the input grid, since there are {quantity_error} {repeated_number}s in the {position_error + 1} {direction}.\nWhich cannot be replaced.")

        for row in range(len(grid)):
            for num in range(1, len(grid) + 1):
                if grid[row].count(num) > 1:
                    print_error(row, num, 'row', grid[row].count(num))
                    return True

                if [grid[j][row] for j in range(len(grid))].count(num) > 1:
                    print_error(row, num, 'column', [grid[j][row] for j in range(len(grid))].count(num))
                    return True
        return False
    
    @staticmethod
    def validate_upright_horizontal_moviment(grid, row, column, num):
        return num in grid[row] or num in [grid[i][column] for i in range(len(grid))]
    
    @staticmethod
    def validate_subgrid_moviment(grid, row, column, num):
        block_size = int(len(grid) ** 0.5)
        block_start_row, block_start_col = block_size * (row // block_size), block_size * (column // block_size)

        return not any(num == grid[block_start_row + i][block_start_col + j] for i in range(block_size) for j in range(block_size))

class SudokuSolution:
    @staticmethod
    def locate_blank_house(grid):
        for row in range(len(grid)):
            for column in range(len(grid)):
                if grid[row][column] == 0:
                    return row, column
        return None, None
    
    @staticmethod
    def solve_sudoku(grid):
        row, column = SudokuSolution.locate_blank_house(grid)

        if row is None and column is None:
            return True
        
        for num in range(1, len(grid) + 1):
            if not SudokuValidate.validate_upright_horizontal_moviment(grid, row, column, num) and \
                    SudokuValidate.validate_subgrid_moviment(grid, row, column, num):
                grid[row][column] = num

                if SudokuSolution.solve_sudoku(grid):
                    return True
                grid[row][column] = 0

def main():
    if not SudokuValidate.verify_repeated_numbers(GRID):
        SudokuPrint.complete_sudoku(GRID)
        
if __name__ == "__main__":
    main()
