import pygame
from board import Board
from constants import BLACK, WHITE, GREEN, SQUARE_SIZE

class Game:
    def __init__(self, win):
        """
        Initializes the Game object.

        Args:
            win: Pygame window object.
        """
        self._init()
        self.win = win

    def update(self):
        """
        Updates the game state and redraws the board.

        This method is responsible for updating the display after each move.
        """
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def _init(self):
        """
        Initializes the game state.

        This method resets various attributes for a new game or when starting the game.
        """
        self.selected = None
        self.board = Board()
        self.turn = BLACK
        self.valid_moves = {}

    def winner(self):
        """
        Checks for the winner of the game.

        Returns:
            tuple or None: Returns a tuple indicating the winner color (BLACK or WHITE),
                           or None if there is no winner yet.
        """
        return self.board.winner()

    def reset(self):
        """
        Resets the game to its initial state.

        This method can be called to start a new game by resetting all game-related attributes.
        """
        self._init()

    def select(self, row, col):
        """
        Handles the selection of a piece on the board.

        Args:
            row (int): The row of the selected position.
            col (int): The column of the selected position.

        Returns:
            bool: True if a piece is successfully selected, False otherwise.
        """
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)

        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True

        return False

    def _move(self, row, col):
        """
        Handles the movement of a selected piece to a new position.

        Args:
            row (int): The row of the target position.
            col (int): The column of the target position.

        Returns:
            bool: True if the move is successful, False otherwise.
        """
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False

        return True

    def draw_valid_moves(self, moves):
        """
        Draws circles to highlight valid moves on the board.

        Args:
            moves (dict): Dictionary containing valid moves as keys.
        """
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, GREEN, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 15)

    def change_turn(self):
        """
        Changes the turn from one player to the other.

        Resets the valid moves for the new player's turn.
        """
        self.valid_moves = {}
        if self.turn == BLACK:
            self.turn = WHITE
        else:
            self.turn = BLACK

    def get_board(self):
        """
        Gets the current game board.

        Returns:
            Board: The current game board.
        """
        return self.board

    def ai_move(self, board):
        """
        Updates the game state with the AI's move.

        Args:
            board (Board): The new game board state after the AI's move.
        """
        self.board = board
        self.change_turn()
