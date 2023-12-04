from sudoku_validate import SudokuValidate
from sudoku_print import SudokuPrint
import pygame
from pygame.locals import QUIT, KEYDOWN, K_SPACE

# Define the Sudoku grid
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

# Define constants for the GUI
WIDTH, HEIGHT = 540, 540
CELL_SIZE = WIDTH // len(GRID)
BLOCK_SIZE = 3
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define the Sudoku class
class Sudoku:
    def __init__(self):
        # Initialize Pygame
        pygame.init()
        # Create a Pygame window with name Stage Sudoku
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Stage Sudoku")
        # Set window icon
        icon = pygame.image.load("./asset/icon.png")
        pygame.display.set_icon(icon)
    
    def draw_grid_line(self, start, end, is_bold):
        line_thickness = 2 if is_bold else 1
        pygame.draw.line(self.screen, BLACK, start, end, line_thickness)

    # Method to draw the Sudoku grid on the screen
    def draw_grid(self, grid):
        self.screen.fill(WHITE)
        for i in range(len(GRID) + 1):
            # Draw horizontal line
            self.draw_grid_line((0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), i % BLOCK_SIZE == 0)
            # Draw vertical line
            self.draw_grid_line((i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), i % BLOCK_SIZE == 0)

        font = pygame.font.Font(None, 36)
        for row in range(len(GRID)):
            for col in range(len(GRID)):
                cell_value = grid[row][col]
                cell_x = col * CELL_SIZE
                cell_y = row * CELL_SIZE
                if cell_value != 0:
                    text = font.render(str(cell_value), True, BLACK)
                    text_rect = text.get_rect(center=(cell_x + CELL_SIZE // 2, cell_y + CELL_SIZE // 2))
                    self.screen.blit(text, text_rect)
                    self.screen.blit(text, text_rect)

    # Method to run the Sudoku game loop
    def run(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                # Handle quit event
                if event.type == QUIT:
                    running = False
                # Handle key press event for spacebar to complete Sudoku if no repeated numbers
                elif event.type == KEYDOWN and event.key == K_SPACE and not SudokuValidate.verify_repeated_numbers(GRID):
                    SudokuPrint.complete_sudoku(GRID)
            # Draw the grid on the screen
            self.draw_grid(GRID)
            pygame.display.flip()
            # Running in 30 FPS
            clock.tick(30)
        pygame.quit()

def main():
    gui = Sudoku()
    gui.run()

if __name__ == "__main__":
    main()
