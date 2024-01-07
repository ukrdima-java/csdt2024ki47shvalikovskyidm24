from copy import deepcopy
from constants import WHITE, BLACK

def minimax(position, depth, max_player, game):
    """
    Minimax algorithm implementation for evaluating moves and finding the best move.

    Args:
        position (Board): The current state of the game board.
        depth (int): The depth of the search tree.
        max_player (bool): True if the current player is maximizing, False otherwise.
        game (Game): The game object.

    Returns:
        tuple: A tuple containing the evaluation score and the best move.
    """
    if depth == 0 or position.winner() is not None:
        return position.evaluate(), position

    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(position, WHITE, game):
            evaluation = minimax(move, depth - 1, False, game)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move

        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(position, BLACK, game):
            evaluation = minimax(move, depth - 1, True, game)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move

        return minEval, best_move

def simulate_move(piece, move, board, game, skip):
    """
    Simulate a move on the board.

    Args:
        piece (Piece): The piece to move.
        move (tuple): The target position (row, col).
        board (Board): The current state of the game board.
        game (Game): The game object.
        skip (Piece): The piece to skip over during the move.

    Returns:
        Board: The resulting board after the move is simulated.
    """
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board

def get_all_moves(board, color, game):
    """
    Get all possible moves for a given color on the board.

    Args:
        board (Board): The current state of the game board.
        color (tuple): The color of the pieces to consider.
        game (Game): The game object.

    Returns:
        list: A list of boards representing all possible moves.
    """
    moves = []

    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)

    return moves