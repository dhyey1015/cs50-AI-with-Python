"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    number_of_x = 0
    number_of_y = 0
    for row in board:
        for cell in row:
            if cell == X:
                number_of_x += 1
            if cell == O:
                number_of_y += 1

    if number_of_x > number_of_y:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_set  = set()
    for i in range(3):
        for j in range(3):
            if(board[i][j] == EMPTY):
                actions_set.add((i, j))
    return actions_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if(action not in actions(board)):
        raise ValueError("Invalid action")
  
    new_board = [row[:] for row in board] # Create a deep copy of the board to avoid modifying the original board
    i, j = action   # Get the row and column from the action
    new_board[i][j] = player(board)  # is determining whether to place "X" or "O" in the cell new_board[i][j] — based on whose turn it is.
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not EMPTY:
            return row[0]                 #[EMPTY, EMPTY, EMPTY] checking this case to avoid index error

    for col in range(3):                                           
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not EMPTY:
            return board[0][col]                               #[EMPTY, EMPTY, EMPTY] checking this case to avoid index error
    
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]                           #[EMPTY, EMPTY, EMPTY] checking this case to avoid index error
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board[0][2] 
    
    return None                          #[EMPTY, EMPTY, EMPTY] checking this case to avoid index error       

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    
    for row in board:
        if EMPTY in row:
            return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win =  winner(board)
    if win == X:
        return 1
    
    elif win == O:
        return -1
    
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
