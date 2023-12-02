import pygame
from pygame.locals import QUIT, KEYDOWN, K_SPACE

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

WIDTH, HEIGHT = 540, 540
CELL_SIZE = WIDTH // len(GRID)

BLOCK_SIZE = 3

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Stage Sudoku")
icon = pygame.image.load("./asset/icon.png")
pygame.display.set_icon(icon)


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

def draw_grid(grid):
    screen.fill(WHITE)

    for i in range(len(GRID) + 1):
        pygame.draw.line(screen, BLACK, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), 2 if i % BLOCK_SIZE == 0 else 1)
        pygame.draw.line(screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), 2 if i % BLOCK_SIZE == 0 else 1)

    font = pygame.font.Font(None, 36)

    for row in range(len(GRID)):
        for col in range(len(GRID)):
            cell_value = grid[row][col]
            cell_x = col * CELL_SIZE
            cell_y = row * CELL_SIZE

            if cell_value != 0:
                text = font.render(str(cell_value), True, BLACK)
                text_rect = text.get_rect(center=(cell_x + CELL_SIZE // 2, cell_y + CELL_SIZE // 2))
                screen.blit(text, text_rect)

def main():
    clock = pygame.time.Clock()
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    if not SudokuValidate.verify_repeated_numbers(GRID):
                        SudokuPrint.complete_sudoku(GRID)

        draw_grid(GRID)
        pygame.display.flip()

        clock.tick(30)
    pygame.quit()

if __name__ == "__main__":
    main()
