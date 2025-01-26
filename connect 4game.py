# Simple Connect Four Game in Python

ROWS = 6
COLS = 7

# Function to create an empty board
def create_board():
    return [[' ' for _ in range(COLS)] for _ in range(ROWS)]

# Function to print the board
def print_board(board):
    for row in board:
        print("|" + "|".join(row) + "|")
    print("-" * (COLS * 2 + 1))

# Function to drop a piece in a column
def drop_piece(board, column, piece):
    for row in range(ROWS - 1, -1, -1):  # Start from the bottom row
        if board[row][column] == ' ':
            board[row][column] = piece
            return row, column
    return None  # If the column is full

# Function to check for a win
def check_win(board, piece):
    # Check horizontal
    for row in range(ROWS):
        for col in range(COLS - 3):
            if all(board[row][col + i] == piece for i in range(4)):
                return True

    # Check vertical
    for row in range(ROWS - 3):
        for col in range(COLS):
            if all(board[row + i][col] == piece for i in range(4)):
                return True

    # Check diagonal (bottom-left to top-right)
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if all(board[row + i][col + i] == piece for i in range(4)):
                return True

    # Check diagonal (top-left to bottom-right)
    for row in range(3, ROWS):
        for col in range(COLS - 3):
            if all(board[row - i][col + i] == piece for i in range(4)):
                return True

    return False

# Main game loop
def play_game():
    board = create_board()
    current_player = 1
    player_piece = 'X'

    while True:
        print_board(board)
        try:
            column = int(input(f"Player {current_player} ({player_piece}), choose a column (0-6): "))
            if column < 0 or column >= COLS:
                print("Invalid column! Please choose a column between 0 and 6.")
                continue
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        move = drop_piece(board, column, player_piece)
        if move is None:
            print("Column is full! Try a different column.")
            continue

        if check_win(board, player_piece):
            print_board(board)
            print(f"Player {current_player} ({player_piece}) wins!")
            break

        # Switch players
        current_player = 3 - current_player
        player_piece = 'O' if player_piece == 'X' else 'X'

# Run the game
if __name__ == "__main__":
    play_game()
