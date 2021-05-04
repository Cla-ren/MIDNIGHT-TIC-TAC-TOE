# TIC TAC TOE

board: list[str] = [" ", " ", " ",
                    " ", " ", " ",
                    " ", " ", " "]

current_symbol = "X"
current_player = "player_1"

single_player = True
game_in_progress = True
winner = None

def enter_name():
    global current_player

    name = input("Enter your name: ")
    current_player = name

#   Chooses between single player and multiplayer mode.
def game_mode():
    global single_player

    mode = input("Select 1 or 2: ")
    mode = int(mode)

    while mode not in (1, 2):
        mode = input("Enter a valid input: ")
        mode = int(mode)

    if mode == 1:
        single_player = True
    elif mode == 2:
        single_player = False
    return

# Asks for player's name.
# enter_name()

def cpu():
    return

def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])

def pick_random():
    return

def play_game():
    display_board()

    while game_in_progress:
        select_position(current_symbol)
        check_game_over()
        next_player()

    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")

def select_position(current_symbol):
    print(current_player + "'s turn.")
    position = input("Choose a position from 1-9: ")
    position = int(position)

    while position not in (1, 2, 3, 4, 5, 6, 7, 8, 9):
        position = input("Choose a position from 1-9: ")
        position = int(position)

    position = int(position) - 1

    board[position] = current_symbol
    display_board()

    valid_move = False
    while not valid_move:

        while position not in (1, 2, 3, 4, 5, 6, 7, 8, 9):
            position = input("Choose a position from 1-9: ")
        position = int(position) - 1

        if board[position] == " ":
            valid_move = True
        else:
            print("You can't go there. Go again.")

#    board[position] = current_player
#    display_board()

def check_game_over():
    check_winner()
    check_tie()


def check_winner():
    global winner

    row_winner = check_rows()
    col_winner = check_cols()
    diag_winner = check_diags()

    if row_winner:
        winner = row_winner
    elif col_winner:
        winner = col_winner
    elif diag_winner:
        winner = diag_winner
    else:
        winner = None
    return

def check_rows():
    global game_in_progress

    row_1 = board[0] == board[1] == board[2] != " "
    row_2 = board[3] == board[4] == board[5] != " "
    row_3 = board[6] == board[7] == board[8] != " "

    if row_1 or row_2 or row_3:
        game_in_progress = False

    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_cols():
    global game_in_progress

    col_1 = board[0] == board[3] == board[6] != " "
    col_2 = board[1] == board[4] == board[7] != " "
    col_3 = board[2] == board[5] == board[8] != " "

    if col_1 or col_2 or col_3:
        game_in_progress = False

    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]
    return

def check_diags():
    global game_in_progress

    diag_1 = board[0] == board[4] == board[8] != " "
    diag_2 = board[6] == board[4] == board[2] != " "

    if diag_1 or diag_2:
        game_in_progress = False

    if diag_1:
        return board[0]
    elif diag_2:
        return board[6]
    return

def check_tie():
    global game_in_progress

    if " " not in board:
        game_in_progress = False

    return

def next_player():
    global current_player
    global current_symbol

    if current_symbol == "X":
        current_symbol = "O"
        current_player = "player_2"
    elif current_symbol == "O":
        current_symbol = "X"
        current_player = "player_1"
    return

#   The following lines of code is meant to run the game.
#
#
#

print("***Midnight TIC TAC TOE***")

print("GAME MODES")
print("1. Single player")
print("2. Multiplayer")

game_mode()

#   For testing.
#   print(single_player)

play_game()
