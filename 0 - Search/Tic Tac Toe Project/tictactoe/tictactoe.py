"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None

testBoard =[[X, EMPTY, X],
            [EMPTY, O, X],
            [O, O, X]]

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
    numberofEmptyCells = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                numberofEmptyCells += 1

    if numberofEmptyCells == 0:
        return None
    elif numberofEmptyCells%2 == 0:
        return O
    else:
        return X
    
print(f'player: {player(testBoard)}')
    


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actionsSet = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actionsSet.add((i,j))
    return actionsSet

print(f'actions: {actions(testBoard)}')


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i = action[0]
    j = action[1]
    newBoard = board
    if board[i][j] == EMPTY:
        newBoard = copy.deepcopy(board)
        newBoard[i][j] = player(board)
        return newBoard
    raise ValueError("Invalid Action!")

# print(f'result: {result(testBoard,(2,2))}')



def winner(board): #Acho que tá errado algum detalhe
    """
    Returns the winner of the game, if there is one.
    """

    if (board[0][0] == X) and (board[0][1] == X) and (board[0][2] == X):
        return X
    if (board[1][0] == X) and (board[1][1] == X) and (board[1][2] == X):
        return X
    if (board[2][0] == X) and (board[2][1] == X) and (board[2][2] == X):
        return X
    
    if (board[0][0] == X) and (board[1][0] == X) and (board[2][0] == X):
        return X
    if (board[0][1] == X) and (board[1][1] == X) and (board[2][1] == X):
        return X
    if (board[0][2] == X) and (board[1][2] == X) and (board[2][2] == X):
        return X
    
    if (board[0][0] == X) and (board[1][1] == X) and (board[2][2] == X):
        return X
    if (board[0][2] == X) and (board[1][1] == X) and (board[2][0] == X):
        return X
    
    
    if (board[0][0] == O) and (board[0][1] == O) and (board[0][2] == O):
        return O
    if (board[1][0] == O) and (board[1][1] == O) and (board[1][2] == O):
        return O
    if (board[2][0] == O) and (board[2][1] == O) and (board[2][2] == O):
        return O
    
    if (board[0][0] == O) and (board[1][0] == O) and (board[2][0] == O):
        return O
    if (board[0][1] == O) and (board[1][1] == O) and (board[2][1] == O):
        return O
    if (board[0][2] == O) and (board[1][2] == O) and (board[2][2] == O):
        return O
    
    if (board[0][0] == O) and (board[1][1] == O) and (board[2][2] == O):
        return O
    if (board[0][2] == O) and (board[1][1] == O) and (board[2][0] == O):
        return O
    
    return None

print(f"winner: {winner(testBoard)}")
        


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    somewoneWon = winner(board) != None
    allCelsFilled = actions(board) == set()
    if somewoneWon or allCelsFilled:
        return True
    return False

print(f'terminal: {terminal(testBoard)}')


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    gameWinner = winner(board)
    if gameWinner is X:
        return 1
    if gameWinner is O:
        return -1
    return 0

print(f'utility: {utility(testBoard)}')



def maxValue(state):
    if terminal(state):
        return utility(state)
    v = -math.inf
    for action in actions(state):
        v = max(v,minValue(result(state,action)))
    return v

def minValue(state):
    if terminal(state):
        return utility(state)
    v = math.inf
    for action in actions(state):
        v = min(v,maxValue(result(state,action)))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    currentPlayer = player(board)
    avaliableActions = actions(board)

    if currentPlayer == X:
        highestValueAction = (0,0)
        highestValue = -math.inf

        for action in avaliableActions:
            actionResultingState = result(board=board,action=action)
            actionResultingStateValue = minValue(state=actionResultingState)

            if actionResultingStateValue >= highestValue:
                highestValue = actionResultingStateValue
                highestValueAction = action

        return highestValueAction
    
    elif currentPlayer == O:
        lowestValueAction = (0,0)
        lowestValue = math.inf

        for action in avaliableActions:
            actionResultingState = result(board=board,action=action)
            actionResultingStateValue = maxValue(state=actionResultingState)

            if actionResultingStateValue <= lowestValue:
                lowestValue = actionResultingStateValue
                lowestValueAction = action

        return lowestValueAction
    
print(f'optimal move: {minimax(testBoard)}')
        


