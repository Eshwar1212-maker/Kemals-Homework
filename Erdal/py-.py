# Challenge 13 — Full Game Loop

board = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
current_player = "X"
turns = 0

while turns < 9:
    # Print the board
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])
    
    # Ask current player to pick a spot
    spot = int(input(current_player + ", pick a spot (0-8): "))
    
    # Put their symbol in that spot
    board[spot] = current_player
    
    # Switch player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"
    
    turns = turns + 1

print("Game over!")