# Challenge 1

Ask the user to pick a number
Use a while loop to count down to 0
Print each number
When it hits 0, print "Blastoff!"

Example:
Pick a number: 5
5
4
3
2
1
Blastoff!

# Challenge 2

Set a secret number (like 7)
Use a while loop to keep asking "Guess the number:"
If they guess wrong, print "Try again"
If they guess right, print "You got it!" and stop the loop

Example output:

Example:
Guess the number: 3
Try again
Guess the number: 9
Try again
Guess the number: 7
You got it!


# Challenge 3

Start with an empty list called cart
Use a while loop to keep asking "Add an item (or type 'done'):"
If they type something, add it to the cart
If they type "done", stop the loop
At the end, print each item in the cart with a number next to it

Example:
Add an item (or type 'done'): apple
Add an item (or type 'done'): milk
Add an item (or type 'done'): bread
Add an item (or type 'done'): done

Your cart:
1. apple
2. milk
3. bread

# Challenge 4

You're playing a video game and you have 5 lives.

Every time you get hit, you lose one life.

Your job:
1. Make a list with 5 hearts: ["❤️", "❤️", "❤️", "❤️", "❤️"]
2. Keep asking the player "Did you get hit? (yes/no):"
3. If they say "yes", remove one heart from the end of the list
4. Print how many hearts are left
5. If all the hearts are gone, print "Game Over!" and end the game

Hint: Use .pop() to remove the last item from a list

Example:
Hearts: ['❤️', '❤️', '❤️', '❤️', '❤️']
Did you get hit? (yes/no): yes
Hearts: ['❤️', '❤️', '❤️', '❤️']
Did you get hit? (yes/no): yes
Hearts: ['❤️', '❤️', '❤️']
Did you get hit? (yes/no): no
Did you get hit? (yes/no): yes
Hearts: ['❤️', '❤️']
Did you get hit? (yes/no): yes
Hearts: ['❤️']
Did you get hit? (yes/no): yes
Hearts: []
Game Over!

# Challenge 5

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

# Challenge 6 (bonus question)

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

# Challenge 15