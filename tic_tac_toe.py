# Import random to randomly choose starting shape.
import random

# Dictionary representing tic-tac-toe. Entering a matching number will assign whoever's turn it is shape to the number value.
game_board = {'7': ' ', '8': ' ', '9': ' ',
              '4': ' ', '5': ' ', '6': ' ',
              '1': ' ', '2': ' ', '3': ' '}

# This prints the game board, using whatever value is in the key slot, with some lines for the board.  
def gameView(game_board):
    print()
    print(f"{game_board['7']} | {game_board['8']} | {game_board['9']}")
    print("--+---+--")
    print(f"{game_board['4']} | {game_board['5']} | {game_board['6']}")
    print("--+---+--")
    print(f"{game_board['1']} | {game_board['2']} | {game_board['3']}")
    print()

# This function checks all win conditions, and if true, prints message and changes global win status to true.
# There is probably a better way to do this.    
def is_win():
    if game_board["1"] == game_board[move] and game_board["2"] == game_board[move] and game_board["3"] == game_board[move]:
        print(f"{whose_turn} is the winner!")
        return True
    elif game_board["4"] == game_board[move] and game_board["5"] == game_board[move] and game_board["6"] == game_board[move]:
        print(f"{whose_turn} is the winner!")
        return True
    elif game_board["7"] == game_board[move] and game_board["8"] == game_board[move] and game_board["9"] == game_board[move]:
        print(f"{whose_turn} is the winner!")
        return True
    elif game_board["3"] == game_board[move] and game_board["5"] == game_board[move] and game_board["7"] == game_board[move]:
        print(f"{whose_turn} is the winner!")
        return True
    elif game_board["1"] == game_board[move] and game_board["5"] == game_board[move] and game_board["9"] == game_board[move]:
        print(f"{whose_turn} is the winner!")
        return True
    elif game_board["3"] == game_board[move] and game_board["6"] == game_board[move] and game_board["9"] == game_board[move]:
        print(f"{whose_turn} is the winner!")
        return True
    elif game_board["2"] == game_board[move] and game_board["5"] == game_board[move] and game_board["8"] == game_board[move]:
        print(f"{whose_turn} is the winner!")
        return True
    elif game_board["1"] == game_board[move] and game_board["4"] == game_board[move] and game_board["7"] == game_board[move]:
        print(f"{whose_turn} is the winner!")
        return True
    else:
        return False

def check_tie(game_board):
    if ' ' not in game_board.values():
        return True

# Where random.choice picks from.   
x_o = ["x", "o"]
# X user wins.
x_score = 0
# O user wins.
o_score = 0
# Win is set to false until a win condition occurs.
win = False
# Tie same as win
tie = False

# Prompt user for either play or quit.
user_input = input("Welcome to tic-tac-toe: press any key and enter to play (q to quit)")
# Prints game image. (Blank board)
gameView(game_board)
# Picks who goes first.
whose_turn = random.choice(x_o)

# Main game loop.
while user_input != 'q':
    
    if whose_turn == "x":
        # X turn, converts user integer input into string to match game dictionary.
        move = (str(input("X: Enter 1-9 on numpad to make your move: ")))
        # If input isn't in dictionary, and the space is occupied, repeats question. 
        if move not in game_board or game_board[move] != ' ':
            continue
        # If move is valid, changes location to x or o depending on whose turn it is.
        game_board[move] = whose_turn
        # Prints view of game again, with move added.
        gameView(game_board)
        print()
        # Tests win conditions, if True, enters win condition.
        win = is_win()
        if win == True:
            x_score += 1 # Increase score
            print(f"Current Score: X:{x_score} O:{o_score}")
            user_input = input("Play again?: press any key and enter to play (q to quit)")
            if user_input == "q":
                break # Ends main while loop.
            else:
                # Resets game board, prints out fresh board.
                game_board = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}
                gameView(game_board)
                
        tie = check_tie(game_board)
        if tie == True:
            user_input = input("This match ended in a tie! Play again?: press any key and enter to play (q to quit)")
            if user_input == "q":
                break # Ends main while loop.
            else:
                # Resets game board, prints out fresh board.
                game_board = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}
                gameView(game_board)
        # Turn swaps to other player.
        whose_turn = "o"
    else:
        move = (str(input("O: Enter 1-9 on numpad to make your move: ")))
        if move not in game_board or game_board[move] != ' ':
            continue
        game_board[move] = whose_turn
        gameView(game_board)
        print()
        win = is_win()
        if win == True:
            o_score += 1
            print(f"Current Score: X:{x_score} O:{o_score}")
            user_input = input("Play again?: press any key and enter to play (q to quit)")
            if user_input == "q":
                break
            else:
                game_board = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}
                gameView(game_board)
        tie = check_tie(game_board)
        if tie == True:
            user_input = input("This match ended in a tie! Play again?: press any key and enter to play (q to quit)")
            if user_input == "q":
                break # Ends main while loop.
            else:
                # Resets game board, prints out fresh board.
                game_board = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}
                gameView(game_board)
        whose_turn = "x"
# After exiting game, print final score.            
print(f"Final score: X:{x_score} O:{o_score}")   
        
    
        

            
        
        
    

    

