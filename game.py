ALL_SPACES = list("123456789")  # The keys for a TTT board.
X, O, BLANK = "X", "O", " "  # Constants for string values.


def create_board():
    return {space: BLANK for space in ALL_SPACES}


def get_board_str(board):
    return f"""
      {board['1']}|{board['2']}|{board['3']}  1 2 3
      -+-+-
      {board['4']}|{board['5']}|{board['6']}  4 5 6
      -+-+-
      {board['7']}|{board['8']}|{board['9']}  7 8 9"""


def is_valid_space(board, space):
    return space in ALL_SPACES and board[space] == BLANK


def is_winner(board, player):
    s, p = board, player
    return (
        (s["1"] == s["2"] == s["3"] == p)
        or (s["4"] == s["5"] == s["6"] == p)
        or (s["7"] == s["8"] == s["9"] == p)
        or (s["1"] == s["4"] == s["7"] == p)
        or (s["2"] == s["5"] == s["8"] == p)
        or (s["3"] == s["6"] == s["9"] == p)
        or (s["3"] == s["5"] == s["7"] == p)
        or (s["1"] == s["5"] == s["9"] == p)
    )


def is_board_full(board):
    return all(board[space] != BLANK for space in ALL_SPACES)


def update_board(board, space, player):
    board[space] = player


def get_move():
    while True:
        move = input("Enter your move (1-9): ")
        if move in ALL_SPACES:
            return move
        print("Invalid input. Try again.")


def main():
    print("Welcome to tic-tac-toe!")
    board = create_board()
    current_player, next_player = X, O

    while True:
        print(get_board_str(board))
        print(f"{current_player}'s move:")
        move = get_move()

        if not is_valid_space(board, move):
            print("Space occupied! Try again.")
            continue

        update_board(board, move, current_player)

        if is_winner(board, current_player):
            print(get_board_str(board))
            print(f"{current_player} wins!")
            break
        elif is_board_full(board):
            print(get_board_str(board))
            print("It's a tie!")
            break

        current_player, next_player = next_player, current_player

    print("Thanks for playing!")


if __name__ == "__main__":
    main()
