import random
game_board = {'7': ' ', '8': ' ', '9': ' ',
              '4': ' ', '5': ' ', '6': ' ',
              '1': ' ', '2': ' ', '3': ' '}
    
def gameView(game_board):
    print()
    print(f"{game_board['7']} | {game_board['8']} | {game_board['9']}")
    print("--+---+--")
    print(f"{game_board['4']} | {game_board['5']} | {game_board['6']}")
    print("--+---+--")
    print(f"{game_board['1']} | {game_board['2']} | {game_board['3']}")
    print()
    
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


    
x_o = ["x", "o"]
x_score = 0
o_score = 0
win = False

user_input = input("Welcome to tic-tac-toe: press any key and enter to play (q to quit)")
gameView(game_board)
whose_turn = random.choice(x_o)
while user_input != 'q':
    if whose_turn == "x":
        move = input("X: Enter 1-9 on numpad to make your move: ")
        game_board[move] = whose_turn
        gameView(game_board)
        print()
        win = is_win()
        if win == True:
            x_score += 1
            print(f"Current Score: X:{x_score} O:{o_score}")
            user_input = input("Play again?: press any key and enter to play (q to quit)")
            if user_input == "q":
                break
            else:
                game_board = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}
                gameView(game_board)
        whose_turn = "o"
    else:
        move = input("O: Enter 1-9 on numpad to make your move: ")
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
        whose_turn = "x"
            
print(f"Final score: X:{x_score} O:{o_score}")   
        
    
        

            
        
        
    

    

