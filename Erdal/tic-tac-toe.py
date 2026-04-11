import random

board = [' '] * 9

def draw_board():
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('-+-+-')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-+-+-')
    print(board[6] + '|' + board[7] + '|' + board[8])

wins = [[0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]]

def check_winner():
    for combo in wins:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
            return board[combo[0]]
    return None

def is_full():
    return ' ' not in board

def player_move():
    while True:
        spot = int(input("Pick a spot (0-8): "))
        if spot < 0 or spot > 8:
            print("Pick a number 0-8")
        elif board[spot] != ' ':
            print("That spot is taken")
        else:
            board[spot] = 'X'
            break

def computer_move():
    available = [i for i in range(9) if board[i] == ' ']
    spot = random.choice(available)
    board[spot] = 'O'
    print(f"Computer picked spot {spot}")

draw_board()

while True:
    player_move()
    draw_board()
    if check_winner():
        print("You win!")
        break
    if is_full():
        print("Draw!")
        break

    computer_move()
    draw_board()
    if check_winner():
        print("Computer wins!")
        break
    if is_full():
        print("Draw!")
        break