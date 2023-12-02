from sudoku_validate import SudokuValidate
from sudoku_print import SudokuPrint
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
