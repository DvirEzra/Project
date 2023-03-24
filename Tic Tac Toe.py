import board as board

player_1 = input("enter the name of player No' 1 : ")
player_2 = input("enter the name of player No' 2 : ")


def print_Welcone_Player(name_1, name_2):
    print(f"Welcome {name_1} and {name_2}")


def print_board(board):
    """Prints the current board state"""
    print("-------------")
    for i in range(3):
        print("|", board[i][0], "|", board[i][1], "|", board[i][2], "|")
        print("-------------")


def get_move(player):
    """Gets a valid move from the specified player"""
    while True:
        row = int(input(f"Enter row (0-2) for player {player}: "))
        col = int(input(f"Enter column (0-2) for player {player}: "))
        if row < 0 or row > 2 and col < 0 or col > 2:
            print("You must enter a row and col number between 0-2.")
        elif row < 0 or row > 2:
            print("You must enter a row number between 0-2.")
        elif col < 0 or col > 2:
            print("You must enter a col number between 0-2.")
        elif board[row][col] != "_":
            print("Slot already taken. Try again.")
        else:
            return row, col


def check_win(board, player):
    """Checks if the specified player has won the game"""
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False


def play_again():
    """Asks if the players want to play again"""
    return input("Do you want to play again? (y/n): ").lower()=='y'


print_Welcone_Player(player_1, player_2)


# Main game loop
while True:
    # Initialize the board
    board = [["_"] * 3 for _ in range(3)]
    print_board(board)

    # Game loop for a single game
    while True:
        # Player X's turn
        row, col = get_move("X")
        board[row][col] = "X"
        print_board(board)
        if check_win(board, "X"):
            print("X wins!")
            break
        if all(board[i][j] != "_" for i in range(3) for j in range(3)):
            print("Draw!")
            break

        # Player O's turn
        row, col = get_move("O")
        board[row][col] = "O"
        print_board(board)
        if check_win(board, "O"):
            print("O wins!")
            break

    # Ask if the players want to play again
    if not play_again():
        break