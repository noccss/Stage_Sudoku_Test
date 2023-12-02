grid = [
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

class SudokuValidate:
    @staticmethod
    def verify_repeated_numbers(grid):
        for row in range(len(grid)):
            for num in range(1, len(grid) + 1):
                if grid[row].count(num) > 1:
                    return True, row, num, 'row', grid[row].count(num)

                if [grid[j][row] for j in range(len(grid))].count(num) > 1:
                    return True, row, num, 'column', [grid[j][row] for j in range(len(grid))].count(num)
        return False, None, None, None, None


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
            print("Blank house is over")
            return True
        
def main():
    has_repeated, position_error, repeated_number, direction, quantity_error = SudokuValidate.verify_repeated_numbers(grid)

    if not has_repeated:
        SudokuSolution.solve_sudoku(grid)
    else:
        print(has_repeated)
        print("Explanation:")
        print(f"There does not exist a valid Sudoku for the input grid, since there are {quantity_error} {repeated_number}s in the {position_error + 1} {direction}.\nWhich cannot be replaced.")

        
if __name__ == "__main__":
    main()
