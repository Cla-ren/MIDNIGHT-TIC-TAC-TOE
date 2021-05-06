#   Midnight TIC TAC TOE
#
#
#

import random

board: list[str] = [" ", " ", " ",
                    " ", " ", " ",
                    " ", " ", " "]

current_symbol = "X"
current_player = "player_1"
following_player = "player_2"

player_1 = "player_1"
player_2 = "player_2"

single_player = True
game_in_progress = True
winner = None
sin_switch = None
mul_switch = None

player_1_score = 0
player_2_score = 0

#   Enter name for single player mode.
def sin_enter_name():
    global player_1
    global player_2

    player_1 = input("Enter your name: ")
    player_2 = "CPU"

#   Enter name for multiplayer name.
def mul_enter_name():
    global player_1
    global player_2

    player_1 = input("Player 1 name: ")
    player_2 = input("Player 2 name: ")

#   For playing again in single player mode.
def sin_play_again():
    global game_in_progress
    global sin_switch

    sin_switch = input("Play again? ")
    print("1. Yes")
    print("2. No")

    while sin_switch.isdigit() == False:
        sin_switch = input("Invalid choice. Choose 1 or 2: ")

    sin_switch = int(sin_switch)

    while sin_switch not in (1, 2):
        sin_switch = input("Invalid choice. Choose 1 or 2: ")

        while sin_switch.isdigit() == False:
            sin_switch = input("Invalid choice. Choose 1 or 2: ")

        sin_switch = int(sin_switch)

    if sin_switch == 1:
        game_in_progress = True
        board[0] = " "
        board[1] = " "
        board[2] = " "
        board[3] = " "
        board[4] = " "
        board[5] = " "
        board[6] = " "
        board[7] = " "
        board[8] = " "

    else:
        print("See you next time! ")

    while sin_switch == 1:
        singleplayer()

#   For playing again in multiplayer mode.
def mul_play_again():
    global game_in_progress
    global mul_switch

    mul_switch = input("Play again? ")
    print("1. Yes")
    print("2. No")

    while mul_switch.isdigit() == False:
        mul_switch = input("Invalid choice. Choose 1 or 2: ")

    mul_switch = int(mul_switch)

    while mul_switch not in (1, 2):
        mul_switch = input("Invalid choice. Choose 1 or 2: ")

        while mul_switch.isdigit() == False:
            mul_switch = input("Invalid choice. Choose 1 or 2: ")

        mul_switch = int(mul_switch)

    if mul_switch == 1:
        game_in_progress = True
        board[0] = " "
        board[1] = " "
        board[2] = " "
        board[3] = " "
        board[4] = " "
        board[5] = " "
        board[6] = " "
        board[7] = " "
        board[8] = " "

    else:
        print("See you next time! ")

    while mul_switch == 1:
        multiplayer()

#   Displays the scores after every game.
def scoreboard():
    global player_1_score
    global player_2_score

    player_1_score = str(player_1_score)
    player_2_score = str(player_2_score)

    print(player_1 + " - " + player_1_score)
    print(player_2 + " - " + player_2_score)

    player_1_score = int(player_1_score)
    player_2_score = int(player_2_score)

#   Runs single player mode.
def singleplayer():
    sin_play_game()
    sin_play_again()

#   Runs multiplayer mode.
def multiplayer():
    mul_play_game()
    mul_play_again()

#   Runs the game in single player mode.
def sin_play_game():
    global player_1_score
    global player_2_score

    display_board()

    while game_in_progress:
        sin_select_position(current_symbol)
        check_game_over()
        next_player()

    if winner == "X":
        print(player_1 + " wins.")
        player_1_score = player_1_score + 1
    elif winner == "O":
        print(player_2 + " wins.")
        player_2_score = player_2_score + 1
    elif winner == None:
        print("Tie.")

    scoreboard()

#   Runs the game in multiplayer mode.
def mul_play_game():
    global player_1_score
    global player_2_score

    display_board()

    while game_in_progress:
        mul_select_position(current_symbol)
        check_game_over()
        next_player()

    if winner == "X":
        print(player_1 + " wins.")
        player_1_score = player_1_score + 1
    elif winner == "O":
        print(player_2 + " wins.")
        player_2_score = player_2_score + 1
    elif winner == None:
        print("Tie.")

    scoreboard()

#   Displays the numbers and their corresponding positions on the board.
def number_position():
    print("1|2|3")
    print("4|5|6")
    print("7|8|9")

#   Chooses between single player and multiplayer mode.
def game_mode():
    global single_player

    mode = input("Select 1 or 2: ")

    while mode.isdigit() == False:
        mode = input("Enter a valid input. Select 1 or 2: ")

    mode = int(mode)

    while mode not in (1, 2):
        mode = input("Enter a valid input. Select 1 or 2: ")

        while mode.isdigit() == False:
            mode = input("Enter a valid input. Select 1 or 2: ")

        mode = int(mode)

    if mode == 1:
        single_player = True
    elif mode == 2:
        single_player = False
    return

#   Displays the board.
def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])

#   Places either X or O on the board.
def sin_select_position(current_symbol):
    global current_player

    if current_symbol == "X":
        current_player = player_1
    elif current_symbol == "O":
        current_player = player_2

    print(current_player + "'s turn.")

    if current_player == player_1:
        position = input("Choose a position from 1-9: ")

        while position.isdigit() == False:
            position = input("Choose a position from 1-9: ")

        position = int(position)

        while position not in (1, 2, 3, 4, 5, 6, 7, 8, 9):
            position = input("Choose a position from 1-9: ")

            while position.isdigit() == False:
                position = input("Choose a position from 1-9: ")

            position = int(position)

        position = position - 1

        valid_move = False
        while not valid_move:
            if board[position] == " ":
                valid_move = True
            else:
                position = input("You can't play there. Try again: ")

                while position.isdigit() == False:
                    position = input("Choose a position from 1-9: ")

                position = int(position) - 1

    elif current_player == player_2:
        position = random.randint(1, 9)
        position = position - 1

        valid_move = False
        while not valid_move:
            if board[position] == " ":
                valid_move = True
            else:
                position = random.randint(1, 9)
                position = position - 1

    board[position] = current_symbol
    display_board()

#   Places either X or O on the board.
def mul_select_position(current_symbol):
    global current_player
    global position

    if current_symbol == "X":
        current_player = player_1
    elif current_symbol == "O":
        current_player = player_2

    print(current_player + "'s turn.")
    position = input("Choose a position from 1-9: ")

    while position.isdigit() == False:
        position = input("Enter a valid input. Choose a position from 1-9: ")

    position = int(position)

    while position not in (1, 2, 3, 4, 5, 6, 7, 8, 9):
        position = input("Enter a valid input. Choose a position from 1-9: ")

        while position.isdigit() == False:
            position = input("Enter a valid input. Choose a position from 1-9: ")

        position = int(position)

    position = position - 1

    valid_move = False
    while not valid_move:
        if board[position] == " ":
            valid_move = True
        else:
            position = input("You can't play there. Try again: ")

            while position.isdigit() == False:
                position = input("Enter a valid input. Choose a position from 1-9: ")

            position = int(position) - 1

    board[position] = current_symbol
    display_board()

#   Checks if the game is over.
def check_game_over():
    check_winner()
    check_tie()

#   Checks for a winner.
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

#   Checks for a winner among the rows.
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

# Checks for a winner among the columns.
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

#   Checks for a winner among the diagonals.
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

#   Checks for a tie.
def check_tie():
    global game_in_progress

    if " " not in board:
        game_in_progress = False

    return

#   Switches the player.
def next_player():
    global current_symbol

    if current_symbol == "X":
        current_symbol = "O"
    elif current_symbol == "O":
        current_symbol = "X"
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

if single_player == True:
    print("Single player mode. ")
elif single_player == False:
    print("Multiplayer mode.")

number_position()

if single_player == True:
    sin_enter_name()
    singleplayer()
elif single_player == False:
    mul_enter_name()
    multiplayer()
