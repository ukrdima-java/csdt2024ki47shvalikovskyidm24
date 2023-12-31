import pygame
import serial
import configparser
from constants import WIDTH, HEIGHT, SQUARE_SIZE, WHITE, BLACK, MENU_BUTTON_WIDTH, MENU_BUTTON_HEIGHT
from game import Game
from minimax.algorithm import minimax

arduino = serial.Serial(port='COM6', baudrate=9600, timeout=.1)
FPS = 60
isWhiteAI = False
isBlackAI = False

pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

def receive_config_from_arduino():
    config_str = ""
    while True:
        response = arduino.readline()
        if response != b'':
            config_str += response.decode()
        if ';' in config_str:
            break
    return config_str.replace('\r\n', '')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main_menu(game):
    run_menu = True
    clock_menu = pygame.time.Clock()

    while run_menu:
        clock_menu.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_menu = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                global isWhiteAI
                global isBlackAI
                if 250 <= pos[0] <= 550 and 100 <= pos[1] <= 250:
                    return "game"
                elif 250 <= pos[0] <= 550 and 350 <= pos[1] <= 500:
                    isWhiteAI = True
                    return "game"
                elif 250 <= pos[0] <= 550 and 600 <= pos[1] <= 750:
                    isWhiteAI = True
                    isBlackAI = True
                    return "game"

        WIN.fill((212, 212, 212))

        pygame.draw.rect(WIN, (93, 190, 163), (250, 100, MENU_BUTTON_WIDTH, MENU_BUTTON_HEIGHT))
        font = pygame.font.Font(None, 36)
        text = font.render("Player vs Player", True, (0, 0, 0))
        WIN.blit(text, (300, 150))

        pygame.draw.rect(WIN, (93, 190, 163), (250, 350, MENU_BUTTON_WIDTH, MENU_BUTTON_HEIGHT))
        text = font.render("Player vs AI", True, (0, 0, 0))
        WIN.blit(text, (325, 400))

        pygame.draw.rect(WIN, (93, 190, 163), (250, 600, MENU_BUTTON_WIDTH, MENU_BUTTON_HEIGHT))
        text = font.render("AI   vs   AI", True, (0, 0, 0))
        WIN.blit(text, (335, 650))
        pygame.display.flip()

    pygame.quit()

def main(game):
    config_str = receive_config_from_arduino()
    config_parser = configparser.ConfigParser()
    config_parser.read_string(config_str)
    run_game = True
    make_turn = False
    clock_game = pygame.time.Clock()
    while run_game:
        clock_game.tick(FPS)
        if game.turn == WHITE and isWhiteAI:
            value, new_board = minimax(game.get_board(), 3, WHITE, game)
            game.ai_move(new_board)
            game.turn = BLACK
            make_turn = True
        if game.turn == BLACK and isBlackAI and not make_turn:
            value, new_board = minimax(game.get_board(), 3, BLACK, game)
            game.ai_move(new_board)
            game.turn = WHITE

        if game.winner() is not None:
            winner_color = "Black" if game.winner() == (0, 0, 0) else "White"
            winner_text = f"Winner: {winner_color}"
            run_game = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        if make_turn:
            pygame.time.delay(2000)
        make_turn = False
        game.update()


    run_winner_menu = True
    clock_winner_menu = pygame.time.Clock()

    while run_winner_menu:
        clock_winner_menu.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_winner_menu = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        WIN.fill((212, 212, 212))

        font = pygame.font.Font(None, 36)
        text = font.render(winner_text, True, (0, 0, 0))
        WIN.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    game_object = Game(WIN)
    current_menu = "main_menu"
    while True:
        if current_menu == "main_menu":
            current_menu = main_menu(game_object)
        elif current_menu == "game":
            main(game_object)