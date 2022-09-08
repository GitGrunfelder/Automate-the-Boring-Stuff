# Initializing the board.
rows = ['1', '2', '3', '4', '5', '6', '7', '8']
columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
board = []

# Any given piece must exist in this list. Starts at 0
pieces = {'bpawn':0,'brook':0,'bknight':0,'bbishop':0,'bqueen':0,'bking':0,
          'wpawn':0,'wrook':0,'wknight':0,'wbishop':0,'wqueen':0,'wking':0}

# Variables for max number of pieces per player.
maxs = {'bpawn':8,'wpawn':8,'brook':2,'wrook':2,'bknight':2,'wknight':2,
        'bbishop':2,'wbishop':2,'bqueen':1,'wqueen':1,'bking':1,'wking':1}

# This creates a list with all possible board locations
def create_board():
    for num in rows:
        for letter in columns:
            board.append(num + letter)
            
# This checks given dictionary of 'space:piece'
# to ensure each player has: 
# at least 1 king
# up to max of each type of piece
# each piece is on a valid space
def isValidChessBoard(input_board):
    
    is_valid = True
    
    for position, piece in input_board.items(): # Check each position:piece for correct key:values
        
        if piece not in pieces:
            print("There was a piece entered that isn't part of the game.")
            is_valid = False
            break
         
        pieces[piece] += 1
          
        if position not in board:
            print("This is an invalid board, as one of the spaces doesn't exist.")
            is_valid = False   
        elif piece not in pieces:
            print("There was a piece entered that isn't part of the game.")
            is_valid = False
        elif pieces[piece] > maxs[piece]:
            print(f'Too many {piece}s.')
            is_valid = False
                
    if pieces['wking'] < 1 or pieces['bking'] < 1:
        print('There are not enough kings to play.')
        is_valid = False
                      
    print(f'This game is good to play: {is_valid}')
    

create_board()
isValidChessBoard()

# Test boards.
# #more than 2 kings
# test_1  = {'1a':'bking', '8f':'wking', '2a': 'bking', '5d':'wking'}

# #more than 8 pawns for one side
# test_2 = {'2a':'bpawn', '2b': 'bpawn', '2c':'bpawn', '2d': 'bpawn', '2e': 'bpawn',\
#          '2f': 'bpawn', '2g': 'bpawn', '2h': 'bpawn',\
#          '7a': 'bpawn', '7b': 'wpawn', '8e': 'wking', '1e': 'bking'}

# #more than 16 pieces for one player
# test_3 = {'2a':'bpawn', '2b': 'bpawn', '2c':'bpawn', '2d': 'bpawn', '2e': 'bpawn',\
#          '2f': 'bpawn', '2g': 'bpawn', '2h': 'bpawn',\
#          '1a': 'brook', '1b': 'bknight', '1c': 'bbishop', '1d': 'bqueen', \
#          '1e':'bking', '1f': 'brook', '1g': 'bknight', '1h': 'bbishop', \
#          '3a': 'bpawn', '7b': 'wking', '7c': 'wqueen'}

# #invalid space 9d
# test_4 = {'1a':'bking', '8f':'wking', '1b':'bqueen', '9d': 'wqueen'}

# #names don't begin with 'w' or 'b'
# test_5 = {'1a':'bking', '8f':'wking', '1b':'zqueen', '6d': 'wqueen'}

# #pieces names 
# test_6 = {'1a':'bking', '8f':'wking', '1b':'bqueen', '6d': 'wqueen',\
#           '7b':'wknightt'}

# #too many white rooks
# test_7 = {'1a':'bking', '8f':'wking', '1b':'bqueen', '6d': 'wqueen', \
#           '5c': 'wrook', '8c':'wrook', '7d': 'wrook'}

# #this board should be valid
# test_8 = {'1a':'bking', '8f':'wking', '1b':'bqueen', '6d': 'wqueen', \
#           '5c': 'wrook'}