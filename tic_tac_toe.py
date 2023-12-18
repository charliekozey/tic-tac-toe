import time

current_player = "x"
move_counter = 0
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]


def main():
    print()
    print("✨ tic-tac-toe ✨")
    print()

    get_game_mode()
    print_board()
    game_loop()


def get_game_mode():
    time.sleep(0.5)
    print("Select Game Mode:")
    print()
    print("Human vs Human? Press 1.")
    print("Human vs Computer? Press 2.")

    print()
    game_mode = input(">")
    print()
    time.sleep(1)

    if game_mode == "1":
        print("Now starting Human-vs-Human game.")
        time.sleep(1)
        print()
    elif game_mode == "2":
        print("Human-vs-Computer mode coming soon.")
        time.sleep(1)
        print()
        print("Now starting Human-vs-Human game.")
        time.sleep(1)
        print()
    else:
        print()
        print(">>>>>>>> Select a game mode by pressing 1 or 2. <<<<<<<<")
        get_game_mode()


def game_loop():
    global current_player

    get_move_input(current_player)
    print_board()

    if evaluate_board(current_player):
        print("Game over!")
        print(f"{current_player.upper()} wins! 🎉")
    elif move_counter == 9:
        print("Game over!")
        print("It's a draw.")
    else:
        if current_player == "x":
            current_player = "o"
        elif current_player == "o":
            current_player = "x"
        game_loop()


def get_move_input(player):
    global move_counter

    square_names = {
        "top left": board[0][0],
        "top center": board[0][1],
        "top right": board[0][2],
        "middle left": board[1][0],
        "middle center": board[1][1],
        "middle right": board[1][2],
        "bottom left": board[2][0],
        "bottom center": board[2][1],
        "bottom right": board[2][2],
    }

    print(f"{player}'s turn".upper())
    print("--------")
    print()
    print(f"{player.upper()}, where would you like to move?")
    print()
    print("You can type any of the following:")
    print()
    for key in square_names.keys():
        if square_names[key] == " ":
            print(key)

    print()
    selected_square = input(">")
    print()

    if (
        selected_square in square_names.keys()
        and
        square_names[selected_square] == " "
    ):
        update_square(selected_square)
        move_counter += 1
    else:
        print(">>>>>>>> Invalid input. Try again. <<<<<<<<")
        time.sleep(0.5)
        print()
        get_move_input(player)


def update_square(input_string):
    row = input_string.split()[0]
    column = input_string.split()[1]

    translate = {
        "top": 0,
        "middle": 1,
        "bottom": 2,
        "left": 0,
        "center": 1,
        "right": 2
    }

    board[translate[row]][translate[column]] = current_player


def print_board():
    output = (
        """
         {} | {} | {}
        ---|---|---
         {} | {} | {}
        ---|---|---
         {} | {} | {}
        """.format(
                board[0][0],
                board[0][1],
                board[0][2],
                board[1][0],
                board[1][1],
                board[1][2],
                board[2][0],
                board[2][1],
                board[2][2]
        )
    )

    print(output)


def evaluate_board(player):
    if (
        # 3 in a row:
        board[0][0] == board[0][1] == board[0][2] == player
        or
        board[1][0] == board[1][1] == board[1][2] == player
        or
        board[2][0] == board[2][1] == board[2][2] == player
        or
        # 3 in a column:
        board[0][0] == board[1][0] == board[2][0] == player
        or
        board[0][1] == board[1][1] == board[2][1] == player
        or
        board[0][2] == board[1][2] == board[2][2] == player
        or
        # 3 diagonally:
        board[0][0] == board[1][1] == board[2][2] == player
        or
        board[0][2] == board[1][1] == board[2][0] == player

    ):
        return player


main()