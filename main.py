import pygame
from KubaGame import KubaGame, Player, Board
pygame.font.init()

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

# font constants
CAPTURES_FONT = MARBLES_FONT = pygame.font.SysFont('helvetica', 20)
WINNER_FONT = pygame.font.SysFont('lucidagrande', 80)


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


def draw_indicators(game, winner):
    turn = None
    won = None
    player_a = CAPTURES_FONT.render("Player A - White", True, WHITE)
    player_b = CAPTURES_FONT.render("Player B - Black", True, WHITE)
    player_a_captures = CAPTURES_FONT.render("Red Captures: " + str(game.get_player_a().get_captured()), True, RED)
    player_b_captures = CAPTURES_FONT.render("Red Captures: " + str(game.get_player_b().get_captured()), True, RED)
    player_a_o_cap = CAPTURES_FONT.render("Black Captures: " + str(8 - game.get_board().get_count_black()), True, RED)
    player_b_o_cap = CAPTURES_FONT.render("White Captures: " + str(8 - game.get_board().get_count_white()), True, RED)

    if game.get_current_turn() == game.get_player_a().get_name():
        turn = CAPTURES_FONT.render("Turn: White", True, WHITE)
    elif game.get_current_turn() == game.get_player_b().get_name():
        turn = CAPTURES_FONT.render("Turn: Black", True, WHITE)

    if winner == game.get_player_a().get_name():
        won = WINNER_FONT.render("WINNER: White", True, RED)
    elif winner == game.get_player_b().get_name():
        won = WINNER_FONT.render("WINNER: Black", True, RED)

    WINDOW.blit(player_a, (70, 300))
    WINDOW.blit(player_b, (950, 300))
    WINDOW.blit(player_a_captures, (70, 340))
    WINDOW.blit(player_b_captures, (950, 340))
    WINDOW.blit(player_a_o_cap, (70, 370))
    WINDOW.blit(player_b_o_cap, (950, 370))
    if turn is not None:
        WINDOW.blit(turn, (545, 700))
    if won is not None:
        WINDOW.blit(won, (350, 350))


def setup_window(grid, game, winner):
    WINDOW.fill(BACKGROUND_COLOR)
    draw_grid(grid)
    draw_indicators(game, winner)
    pygame.display.update()


def make_move(game, player, row_md, column_md, row_mu, column_mu):
    direction = None

    if row_mu > row_md:
        direction = 'B'
    if row_mu < row_md:
        direction = 'F'
    if column_mu > column_md:
        direction = 'R'
    if column_mu < column_md:
        direction = 'L'

    return game.make_move(player, (row_md, column_md), direction)


def main():
    run = True
    clock = pygame.time.Clock()

    game = KubaGame(('player_a', 'W'), ('player_b', 'B'))
    setup_window(game.get_board().get_board(), game, game.get_winner())

    column_new_md = None
    row_new_md = None

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
                        if make_move(game, 'player_a', row_new_md, column_new_md, row_new_mu, column_new_mu):
                            setup_window(game.get_board().get_board(), game, game.get_winner())

                    elif game.get_marble((row_new_md, column_new_md)) == 'B':
                        if make_move(game, 'player_b', row_new_md, column_new_md, row_new_mu, column_new_mu):
                            setup_window(game.get_board().get_board(), game, game.get_winner())

        if game.get_winner() is not None:
            setup_window(game.get_board().get_board(), game, game.get_winner())

    main()


if __name__ == "__main__":
    main()
