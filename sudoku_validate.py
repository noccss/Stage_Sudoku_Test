class SudokuValidate:
    @staticmethod
    def verify_repeated_numbers(grid):
        def print_error(position_error, repeated_number, direction, quantity_error):
            print(False)
            print(f"Explanation:\nNo solution exists\nThere does not exist a valid Sudoku for the input grid, since there are {quantity_error} {repeated_number}s in the {position_error + 1} {direction}.\nWhich cannot be replaced.")

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