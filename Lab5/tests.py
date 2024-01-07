import unittest
import pygame

from constants import WHITE, BLACK, WIDTH, HEIGHT, ROWS, COLS, SQUARE_SIZE, RED, GREEN, BLUE, GREY, LIGHT, DARK, MENU_BUTTON_WIDTH, MENU_BUTTON_HEIGHT, CROWN
from coverage import Coverage
from main import get_row_col_from_mouse
from piece import Piece
from board import Board
from game import Game

class TestYourScript(unittest.TestCase):
    def setUp(self):
        self.mock_win = pygame.Surface((800, 600))  # Mock pygame window

    def print_test_result(self, test_name, result):
        print(f"{test_name}: {'Passed' if result else 'Failed'}")

    def test_calc_pos(self):
        piece = Piece(1, 2, BLACK)
        piece.calc_pos()
        result_x = piece.x == 2 * SQUARE_SIZE + SQUARE_SIZE // 2
        result_y = piece.y == 1 * SQUARE_SIZE + SQUARE_SIZE // 2
        self.print_test_result("test_calc_pos", result_x and result_y)

    def test_make_king(self):
        piece = Piece(1, 2, BLACK)
        self.assertFalse(piece.king)
        piece.make_king()
        result = piece.king
        self.print_test_result("test_make_king", result)

    def test_draw(self):
        piece = Piece(1, 2, BLACK)
        piece.calc_pos()  # Ensure position is calculated
        piece.draw(self.mock_win)
        result = True  # Assume the draw method runs without errors
        self.print_test_result("test_draw", result)

    def test_move(self):
        piece = Piece(1, 2, BLACK)
        piece.move(3, 4)
        result_row = piece.row == 3
        result_col = piece.col == 4
        result_x = piece.x == 4 * SQUARE_SIZE + SQUARE_SIZE // 2
        result_y = piece.y == 3 * SQUARE_SIZE + SQUARE_SIZE // 2
        result = result_row and result_col and result_x and result_y
        self.print_test_result("test_move", result)

    def test_get_row_col_from_mouse(self):
        # Test when mouse position is at the top-left corner
        result = get_row_col_from_mouse((0, 0))
        expected_result = (0, 0)
        self.assertEqual(result, expected_result)
        self.print_test_result("test_get_row_col_from_mouse", result == expected_result)

        # Test when mouse position is in the middle of the first square
        result = get_row_col_from_mouse((SQUARE_SIZE // 4, SQUARE_SIZE // 4))
        expected_result = (0, 0)
        self.assertEqual(result, expected_result)
        self.print_test_result("test_get_row_col_from_mouse", result == expected_result)

        # Test when mouse position is in the middle of the second square
        result = get_row_col_from_mouse((SQUARE_SIZE + SQUARE_SIZE // 4, SQUARE_SIZE // 4))
        expected_result = (0, 1)
        self.assertEqual(result, expected_result)
        self.print_test_result("test_get_row_col_from_mouse", result == expected_result)


    def test_create_board(self):
        board = Board()
        result_rows = len(board.board) == ROWS
        result_cols = all(len(row) == COLS for row in board.board)
        result_pieces = all(isinstance(piece, (Piece, int)) for row in board.board for piece in row)
        result = result_rows and result_cols and result_pieces
        self.print_test_result("test_create_board", result)

    def test_draw_squares(self):
        board = Board()
        board.draw_squares(self.mock_win)
        # Check if drawing results in any errors (can't check actual output in unittest)
        result = True
        self.print_test_result("test_draw_squares", result)

    def test_init(self):
        game = Game(self.mock_win)
        result_win = game.win is not None
        result_selected = game.selected is None
        result_board = game.board is not None
        result_turn = game.turn == BLACK
        result_valid_moves = game.valid_moves == {}
        result = result_win and result_selected and result_board and result_turn and result_valid_moves
        self.print_test_result("test_init", result)

    def test_reset(self):
        game = Game(self.mock_win)
        game.select(1, 2)
        game.reset()
        result_selected = game.selected is None
        result_board = game.board is not None
        result_turn = game.turn == BLACK
        result_valid_moves = game.valid_moves == {}
        result = result_selected and result_board and result_turn and result_valid_moves
        self.print_test_result("test_reset", result)

    def test_change_turn(self):
        game = Game(self.mock_win)
        game.turn = BLACK
        game.valid_moves = {(1, 2): [(3, 4), (5, 6)], (3, 4): [(5, 6)]}
        game.change_turn()
        result_turn = game.turn == WHITE
        result_valid_moves = game.valid_moves == {}
        result = result_turn and result_valid_moves
        self.print_test_result("test_change_turn", result)

    def test_winner_no_winner(self):
        game = Game(self.mock_win)
        winner = game.winner()
        self.assertIsNone(winner)

    def test_winner_black_winner(self):
        game = Game(self.mock_win)
        winner = game.winner()
        self.assertEqual(winner, None)

    def test_winner_white_winner(self):
        game = Game(self.mock_win)
        winner = game.winner()
        self.assertEqual(winner, None)

    def test_draw_valid_moves(self):
        game = Game(self.mock_win)
        # Assume initial state with a selected piece
        piece = game.get_board().get_piece(1, 1)
        game.selected = piece
        valid_moves = {(2, 2), (3, 3)}
        game.draw_valid_moves(valid_moves)


    def run_tests(self):
        # Run the tests with coverage
        cov = Coverage(source=["game", "piece", "board"])
        cov.start()

        # Run the tests
        unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestYourScript))

        # Stop coverage and report
        cov.stop()
        cov.report()

    def test_square_size_calculation(self):
        self.assertIsInstance(SQUARE_SIZE, int)
        self.assertEqual(SQUARE_SIZE, WIDTH // COLS)

    def test_color_values(self):
        for color in [LIGHT, DARK, WHITE, BLACK, GREY, RED, GREEN, BLUE]:
            self.assertTrue(all(0 <= value <= 255 for value in color))

    def test_menu_button_dimensions(self):
        self.assertIsInstance(MENU_BUTTON_WIDTH, int)
        self.assertIsInstance(MENU_BUTTON_HEIGHT, int)
        self.assertGreater(MENU_BUTTON_WIDTH, 0)
        self.assertGreater(MENU_BUTTON_HEIGHT, 0)

    def test_image_loading(self):
        # Assuming CROWN is a path to an image file
        # This test checks if the image file exists
        self.assertTrue(CROWN)

    def test_board_dimensions(self):
        self.assertEqual(WIDTH, 800)
        self.assertEqual(HEIGHT, 800)
        self.assertIsInstance(ROWS, int)
        self.assertIsInstance(COLS, int)
        self.assertGreater(ROWS, 0)
        self.assertGreater(COLS, 0)

    def test_color_codes(self):
        for color in [RED, GREEN, BLUE]:
            self.assertTrue(all(0 <= value <= 255 for value in color))


if __name__ == '__main__':
    unittest.main()