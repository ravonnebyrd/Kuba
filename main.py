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


def draw_grid(grid):
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


def setup_window(grid):
    WINDOW.fill(BACKGROUND_COLOR)
    draw_grid(grid)
    pygame.display.update()


def make_move(game, player, coordinates, direction_coordinates):
    direction = None
    row_md, column_md = coordinates
    row_mu, column_mu = direction_coordinates

    if row_mu > row_md:
        direction = 'B'
    if row_mu < row_md:
        direction = 'F'
    if column_mu > column_md:
        direction = 'R'
    if column_mu < column_md:
        direction = 'L'

    return game.make_move(player, coordinates, direction)


def main():
    run = True
    clock = pygame.time.Clock()

    game = KubaGame(('player_a', 'W'), ('player_b', 'B'))
    setup_window(game.get_board().get_board())
    turn = 0

    position_md = None
    column_new_md = None
    row_new_md = None

    position_mu = None
    column_new_mu = None
    row_new_mu = None

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                position_md = pygame.mouse.get_pos()
                row, column = position_md
                column_new_md = int((row - MARGIN_X) / (SQUARE_HEIGHT + SQUARE_MARGIN))
                row_new_md = int((column - MARGIN_Y) / (SQUARE_HEIGHT + SQUARE_MARGIN))

            if event.type == pygame.MOUSEBUTTONUP:
                position_mu = pygame.mouse.get_pos()
                row, column = position_mu
                column_new_mu = int((row - MARGIN_X) / (SQUARE_HEIGHT + SQUARE_MARGIN))
                row_new_mu = int((column - MARGIN_Y) / (SQUARE_HEIGHT + SQUARE_MARGIN))

                if row_new_md != row_new_mu or column_new_md != column_new_mu:
                    if game.get_marble((row_new_md, column_new_md)) == 'W':
                        if make_move(game, 'player_a', (row_new_md, column_new_md), (row_new_mu, column_new_mu)):
                            setup_window(game.get_board().get_board())

                    elif game.get_marble((row_new_md, column_new_md)) == 'B':
                        if make_move(game, 'player_b', (row_new_md, column_new_md), (row_new_mu, column_new_mu)):
                            setup_window(game.get_board().get_board())

        if game.get_winner() is not None:
            run = False

    pygame.quit()


if __name__ == "__main__":
    main()
