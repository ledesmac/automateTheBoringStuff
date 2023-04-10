#! python3
# isValidChessBoard.py - validates that the chessboard is valid and does not have an impossible setup

# In this chapter, we used the dictionary value {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'} 
# to represent a chess board. Write a function named isValidChessBoard() that takes a dictionary argument and returns True or False 
# depending on if the board is valid.
# 
# A valid board will have exactly one black king and exactly one white king. Each player can only have at most 16 pieces, at most 8 pawns, 
# and all pieces must be on a valid space from '1a' to '8h'; that is, a piece can’t be on space '9z'. 
# The piece names begin with either a 'w' or 'b' to represent white or black, followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'. 
# This function should detect when a bug has resulted in an improper chess board.

import re

test_board =  { 'bking':'1h',  'wqueen':'6c', 'bbishop': '2g', 'bqueen': '5h', 'wking': '3e'}
PIECE_NAMES = [
    'bpawn', 'bknight', 'bbishop', 'brook', 'bqueen', 'bking', #black pieces
    'wpawn', 'wknight', 'wbishop', 'wrook', 'wqueen', 'wking' #white pieces
    ]
X_AXIS = ['a','b','c','d','e','f','g','h']
Y_AXIS = [1,2,3,4,5,6,7,8]

PIECE_COUNT = {
    'king' : 1,
    'pawns' : 8,
    'total' : 16
}

    
def isValidChessBoard(board):
    is_valid = True
    #check all piece names are correct
    for key in board.keys():
        if key not in PIECE_NAMES:
            is_valid = False
    
    print(Y_AXIS)
    if is_valid == True :
        for value in board.values():
            print(value)
            if value[1] not in X_AXIS or int(value[0]) not in Y_AXIS:
                is_valid = False
    if is_valid == True :
        for key in

    

isValidChessBoard(test_board)