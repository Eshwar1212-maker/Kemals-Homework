# Challenge 5(already completed)

Right now your Tic-Tac-Toe game has a problem.

If Player X picks spot 4, then Player O can ALSO pick spot 4 and steal it.

That's not fair!

Fix it:
- When a player picks a spot, check if it's empty first
- Empty spots have "_" in them
- If the spot already has an X or O, tell them "That spot is taken! Try again."(use an if statement to check the value of the current spot)
- Keep asking until they pick an empty spot


Example:
X, pick a spot (0-8): 4
(X goes in spot 4)

O, pick a spot (0-8): 4
That spot is taken! Try again.
O, pick a spot (0-8): 4
That spot is taken! Try again.
O, pick a spot (0-8): 2
(O goes in spot 2)

# Challenge 6 (already completed)

Continue from where you left off in the tic tac toe game you created, now you have to track wins

ROWS (3 in a row across):

X | X | X       _ | _ | _       _ | _ | _
_ | _ | _   or  X | X | X   or  _ | _ | _
_ | _ | _       _ | _ | _       X | X | X

Check: board[0], board[1], board[2]
Check: board[3], board[4], board[5]
Check: board[6], board[7], board[8]


COLUMNS (3 in a row down):

X | _ | _       _ | X | _       _ | _ | X
X | _ | _   or  _ | X | _   or  _ | _ | X
X | _ | _       _ | X | _       _ | _ | X

Check: board[0], board[3], board[6]
Check: board[1], board[4], board[7]
Check: board[2], board[5], board[8]


DIAGONALS (3 in a row corner to corner):

X | _ | _       _ | _ | X
_ | X | _   or  _ | X | _
_ | _ | X       X | _ | _

Check: board[0], board[4], board[8]
Check: board[2], board[4], board[6]

# Challenge 7
Watch these sections with the Tech with Tim video that you have. I will link it right over here:

https://www.youtube.com/watch?v=VchuKL44s6E

From that video watch these sections:

01:00:33 — Functions ⭐ (most important, main concept this week)

00:46:02 — While Loops (quick refresher, he just used them)

00:54:29 — Dicts (next concept coming up, get him familiar early)

01:10:42 — Exceptions + 01:11:28 — Handling Exceptions (watch together, helps with debugging)

Also, do as much research online. Your goal should be to master functions. We're going to be using functions a lot. 

# Challenge 8

Challenge — Guess the Number Game

Write a program that picks a secret number (just hardcode it, like secret = 7) and lets the user keep guessing until they get it right.
Your task:

Write a function called check_guess(guess, secret) that returns "too high", "too low", or "correct".

In a while loop, keep asking the user to guess until they get it right.

Use the function to tell them if their guess was too high, too low, or correct.

When they get it right, print how many tries it took them.

Expected output:

Guess the number: 5

Too low!

Guess the number: 9

Too high!

Guess the number: 7


# Challenge 9

Challenge X — Make a print_board() function
Right now, every time you want to show the board, you have to write these 3 lines:
```
print(board[0] + " | " + board[1] + " | " + board[2])
print(board[3] + " | " + board[4] + " | " + board[5])
print(board[6] + " | " + board[7] + " | " + board[8])
```
That's a lot of typing every turn! A function lets you bundle those 3 lines together, give them a name, and then just CALL the name whenever you want to use them.
Your task:

Create a function called print_board() that prints the full board (all 3 rows).
In your while loop, DELETE those 3 print lines and replace them with a single call: print_board()
Run your game and make sure it works exactly the same as before.

Starter hint:

def print_board():
    # put the 3 print lines in here

And then in the same while loop, it should look like
while turns < 9:
    print_board()

# Challenge 10 (🔥BONUS CHALLENGE)

Refactor the Win Check (HARD)

Task: Right now your win check uses 8 separate if statements. That's a LOT of repeated code. Can you make it shorter by using a list?

Hint 1: Make a list of lists where each inner list is a winning combo. Example:
pythonwins = [
    [0, 1, 2],  # top row
    [3, 4, 5],  # middle row
    # ... fill in the rest (there are 8 total)
]
Hint 2: Use a for loop to go through each combo in wins. Inside the loop, check if board[combo[0]], board[combo[1]], and board[combo[2]] are all equal to current_symbol.

Hint 3: If you find a winner inside the loop, set a variable like winner = current_symbol and use break to stop the loop.
Why this matters: This is called refactoring — making code shorter and cleaner without changing what it does. Real developers do this constantly. You're turning 8 repeated blocks into 1 loop. That's a huge skill.

Success criteria: Your game works EXACTLY the same as before, but the win-check section is way shorter.