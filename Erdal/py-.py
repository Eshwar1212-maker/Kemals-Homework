# Challenge 13 — Full Game Loop
board = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
current_symbol = "X"
turns = 0
while turns < 9:
    # Print the board
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])
    # 1. Get the input as TEXT (no int() here!)
    spot = input(current_symbol + ", pick a spot (0-8): ")
    # 2. The "Trap" — keep asking if it's not a number
    while not spot.isdigit():
        print("That is not a number!")
        spot = input(current_symbol + ", pick a spot (0-8): ")
    # 3. Safe zone! Now we turn it into an integer
    spot = int(spot)
    # 4. Is the spot already taken? Keep asking until they pick an empty one
    while board[spot] != "_":
        print("That spot is already taken!")
        spot = input(current_symbol + ", pick a spot (0-8): ")
        while not spot.isdigit():
            print("That is not a number!")
            spot = input(current_symbol + ", pick a spot (0-8): ")
        spot = int(spot)
    # Put their symbol in that spot
    board[spot] = current_symbol

    # Check for a win (BEFORE switching player!)
    if board[0] == current_symbol and board[1] == current_symbol and board[2] == current_symbol:
        print(current_symbol + " wins!")
        break
    if board[3] == current_symbol and board[4] == current_symbol and board[5] == current_symbol:
        print(current_symbol + " wins!")
        break
    if board[6] == current_symbol and board[7] == current_symbol and board[8] == current_symbol:
        print(current_symbol + " wins!")
        break
    if board[0] == current_symbol and board[3] == current_symbol and board[6] == current_symbol:
        print(current_symbol + " wins!")
        break
    if board[1] == current_symbol and board[4] == current_symbol and board[7] == current_symbol:
        print(current_symbol + " wins!")
        break
    if board[2] == current_symbol and board[5] == current_symbol and board[8] == current_symbol:
        print(current_symbol + " wins!")
        break
    if board[0] == current_symbol and board[4] == current_symbol and board[8] == current_symbol:
        print(current_symbol + " wins!")
        break
    if board[2] == current_symbol and board[4] == current_symbol and board[6] == current_symbol:
        print(current_symbol + " wins!")
        break

    # Switch player
    if current_symbol == "X":
        current_symbol = "O"
    else:
        current_symbol = "X"
    turns = turns + 1
print("Game over!")