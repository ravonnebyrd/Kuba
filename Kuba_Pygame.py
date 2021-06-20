import pygame
from KubaGame import KubaGame, Player, Board


# setting the window
WIDTH, HEIGHT = 1200, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Play Kuba!')

# color constants
BLACK = (30, 30, 30)
BLACK_BACKGROUND = (41, 41, 41)
GREY = (128, 128, 128)
RED = (214, 78, 70)
WHITE = (230, 230, 230)
YELLOW = (255, 255, 0)

BACKGROUND_COLOR = BLACK_BACKGROUND
SQUARE_COLOR = (255, 255, 255)

# grid constants
MARGIN_X = 313
MARGIN_Y = 113
SQUARE_WIDTH = SQUARE_HEIGHT = 80
SQUARE_MARGIN = 2
COLUMNS = ROWS = 7

FPS = 60


def draw_square(left_pos, top_pos, width, height):
    return pygame.Rect(left_pos, top_pos, width, height)


def draw_circle(circle_color, center, radius, width=0):
    return pygame.draw.circle(WINDOW, circle_color, center, radius, width)


def draw_grid():
    board = Board()
    grid = board.get_board()

    left = MARGIN_X
    top = MARGIN_Y

    for row in range(ROWS):
        for column in range(COLUMNS):
            square = draw_square(left, top, SQUARE_WIDTH, SQUARE_HEIGHT)
            pygame.draw.rect(WINDOW, SQUARE_COLOR, square)

            if grid[row][column] == 'R':
                draw_circle(RED, ((left + SQUARE_WIDTH / 2), (top + SQUARE_HEIGHT / 2)), 30)
            if grid[row][column] == 'B':
                draw_circle(BLACK, ((left + SQUARE_WIDTH / 2), (top + SQUARE_HEIGHT / 2)), 30)
            if grid[row][column] == 'W':
                draw_circle(WHITE, ((left + SQUARE_WIDTH / 2), (top + SQUARE_HEIGHT / 2)), 30)

            left = left + SQUARE_WIDTH + SQUARE_MARGIN
        left = MARGIN_X
        top = top + SQUARE_HEIGHT + SQUARE_MARGIN


def setup_window():
    WINDOW.fill(BACKGROUND_COLOR)
    draw_grid()
    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                row, column = position
                column_new = int((row - MARGIN_X) / (SQUARE_HEIGHT + SQUARE_MARGIN))
                row_new = int((column - MARGIN_Y) / (SQUARE_HEIGHT + SQUARE_MARGIN))
                print('Row: ', row_new, ', Column: ', column_new)

        setup_window()

    pygame.quit()


if __name__ == "__main__":
    main()
