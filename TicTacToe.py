player1 = 'X'
player2 = 'O'


def instruction_how_to_play():  # instruction how to play

    print("Welcome in Tic Tac Toe by Paul:")
    print("This is instruction how to enter marks:")
    print("\n")
    print("\t     |     |")
    print("\t  1  |  2  |  3")
    print('\t_____|_____|_____')
    print("\t     |     |")
    print("\t  4  |  5  |  6")
    print('\t_____|_____|_____')
    print("\t     |     |")
    print("\t  7  |  8  |  9")
    print("\t     |     |")
    print("\n")


def display_board(board):  # display board
    print("Here is the current board:")
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(board[1], board[2], board[3]))
    print('\t_____|_____|_____')
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(board[4], board[5], board[6]))
    print('\t_____|_____|_____')
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(board[7], board[8], board[9]))
    print("\t     |     |")
    print("\n")


def position_choice(board):  # choose position

    choice = 0

    while choice not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, choice):

        try:
            choice = int(input("Choose a position ( 1 - 9 ): "))

            if choice not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, choice):
                print("Sorry, but you did not choose valid position")
        except ValueError:
            print("Sorry, i dont understand. You can choose only position ( 1 - 9 )")

    return choice


def player_turns(total_turns):  # choose with one player is playing

    if total_turns % 2 == 0:
        total_turns += 1
        return player2
    else:
        return player1


def space_check(board, position):  # check if position is free

    return board[position] == " "


def replacement_choice_x(game_list, position):  # replace position with X

    user_placement = ''
    right_choice = ['X', 'x']

    while user_placement not in right_choice:

        user_placement = input("Type X: ")

        if user_placement not in right_choice:
            print("Sorry, but u can choose only X")

    game_list[position] = user_placement

    return game_list


def replacement_choice_o(game_list, position):  # replace position with O

    user_placement = ''
    right_choice = ['O', 'o']

    while user_placement not in right_choice:

        user_placement = input("Type O: ")

        if user_placement not in right_choice:
            print("Sorry, but u can choose only O")

    game_list[position] = user_placement

    return game_list


def next_game():
    choice = ''
    right_choice = ['Y', 'y']
    mixed_choice = ['Y', 'N', 'y', 'n']

    while choice not in mixed_choice:

        choice = input("Do you want play another game?: (Y or N) ")

        if choice not in mixed_choice:
            print("Sorry, i don't understand please choose Y or N")

    if choice in right_choice:
        lunch_game()
    else:
        print("Thanks for playing")
        quit()


def win_check(board):  # check if someone win
    if board[1] == board[2] == board[3] == player1 or board[1] == board[2] == board[3] == player2:
        print("Congratulation {}-{}-{} horizontally in top row is a winning move!"
              .format(board[1], board[2], board[3]))
        next_game()
    elif board[4] == board[5] == board[6] == player1 or board[4] == board[5] == board[6] == player2:
        print("Congratulation {}-{}-{} horizontally in middle row is a winning move!"
              .format(board[4], board[5], board[6]))
        next_game()
    elif board[7] == board[8] == board[9] == player1 or board[7] == board[8] == board[9] == player2:
        print("Congratulation {}-{}-{} horizontally in bottom row is a winning move!"
              .format(board[7], board[8], board[9]))
        next_game()
    elif board[1] == board[5] == board[9] == player1 or board[1] == board[5] == board[9] == player2:
        print("Congratulation {}-{}-{} cross striking is a winning move!"
              .format(board[1], board[5], board[9]))
        next_game()
    elif board[7] == board[5] == board[3] == player1 or board[7] == board[5] == board[3] == player2:
        print("Congratulation {}-{}-{} cross striking is a winning move!"
              .format(board[7], board[5], board[3]))
        next_game()
    elif board[1] == board[4] == board[7] == player1 or board[1] == board[4] == board[7] == player2:
        print("Congratulation {}-{}-{} vertically in first row is a winning move!"
              .format(board[1], board[4], board[7]))
        next_game()
    elif board[2] == board[5] == board[8] == player1 or board[2] == board[5] == board[8] == player2:
        print("Congratulation {}-{}-{} vertically in second row is a winning move!"
              .format(board[2], board[5], board[8]))
        next_game()
    elif board[3] == board[6] == board[9] == player1 or board[3] == board[6] == board[9] == player2:
        print("Congratulation {}-{}-{} vertically in third row a winning move!"
              .format(board[3], board[6], board[9]))
        next_game()


def draw_check(turns):  # check if game is draw

    if turns == 9:
        print("DRAW - try again")
        next_game()


def lunch_game():  # lunch game

    game_on = True
    game_board = [" "]*10

    instruction_how_to_play()

    while game_on:
        display_board(game_board)
        for turns in range(1, 10):

            if player_turns(turns) == player1:

                print("Player One. Turn: {}".format(turns))

                position = position_choice(game_board)

                game_board = replacement_choice_x(game_board, position)

                display_board(game_board)

                win_check(game_board)

                draw_check(turns)

            elif player_turns(turns) == player2:
                print("Player Two. Turn: {}".format(turns))

                position = position_choice(game_board)

                game_board = replacement_choice_o(game_board, position)

                display_board(game_board)

                win_check(game_board)

                draw_check(turns)


lunch_game()
