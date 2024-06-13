# 1. Define the Game Board
board = [["1", "2", "3"],
         ["4", "5", "6"],
         ["7", "8", "9"]]

# 2. Display the Game Board
def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# 3. Player Input
def player_input(player):
    while True:
        try:
            choice = int(input(f"Player {player}, enter a number (1-9): ")) - 1
            row, col = divmod(choice, 3)
            if board[row][col] not in ["X", "O"]:
                board[row][col] = player
                break
            else:
                print("Cell already taken, choose another.")
        except (ValueError, IndexError):
            print("Invalid input, please enter a number between 1 and 9.")

# 4. Game Logic
def check_win(player):
    # Check rows
    for row in board:
        if all(s == player for s in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def check_draw():
    return all(all(cell in ["X", "O"] for cell in row) for row in board)

# 5. Game Loop
def main():
    current_player = "X"
    while True:
        display_board(board)
        player_input(current_player)
        if check_win(current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break
        elif check_draw():
            display_board(board)
            print("It's a draw!")
            break
        current_player = "O" if current_player == "X" else "X"

# 6. End Game
if __name__ == "__main__":
    main()
