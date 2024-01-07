import pygame

from constants import SQUARE_SIZE, CROWN

class Piece:
    PADDING = 15
    OUTLINE = 2

    def __init__(self, row, col, color):
        """
        Initializes a Piece object.

        Args:
            row (int): The row position of the piece on the board.
            col (int): The column position of the piece on the board.
            color: The color of the piece (BLACK or WHITE).
        """
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        """Calculates the pixel position of the piece on the window."""
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        """Marks the piece as a king."""
        self.king = True

    def draw(self, win):
        """
        Draws the piece on the window.

        Args:
            win: Pygame window object.
        """
        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(win, self.color, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width() // 2, self.y - CROWN.get_height() // 2))

    def move(self, row, col):
        """
        Moves the piece to a new position on the board.

        Args:
            row (int): The new row position.
            col (int): The new column position.
        """
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):
        """Returns a string representation of the piece's color."""
        return self.color