grid = [
    [3, 3, 6, 5, 7, 8, 4, 9, 2],
    [5, 2, 1, 1, 1, 1, 1, 1, 1],
    [1, 8, 7, 1, 1, 1, 1, 3, 1],
    [1, 1, 3, 1, 1, 1, 1, 8, 1],
    [9, 1, 1, 8, 6, 3, 1, 1, 5],
    [1, 5, 1, 1, 9, 1, 6, 1, 1],
    [1, 3, 1, 1, 1, 1, 2, 5, 1],
    [1, 1, 1, 1, 1, 1, 1, 7, 4],
    [1, 1, 5, 2, 1, 6, 3, 1, 1]
]

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
    SudokuSolution.solve_sudoku(grid)
        
if __name__ == "__main__":
    main()