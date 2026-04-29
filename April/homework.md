# Week 3 - Hangman

## Use these sections in the Tech With Tim Video, reference them if you get stuck as well during the challenges

https://www.youtube.com/watch?v=VchuKL44s6E

1. 00:41:32 — For Loops

→ Needed for Challenge 1 (looping through the string "python") AND Challenge 4 (looping through the secret word to print underscores)

2. 00:22:19 — Conditional Operators
→ Needed for Challenge 2 — this is where the in keyword lives (if letter in word:)

3. 00:46:02 — While Loops
→ Needed for Challenge 3 (keep asking for letters until they type "done")

4. 00:35:41 — List/Tuples
→ Needed for Challenge 3 (.append() to add letters to the list)

# Challenge 1 — Loop Through a String

A string is just a list of letters! You can loop through it just like a list.

Your task:
Write a for loop that goes through the word "python" and prints each letter 
on its own line.

Expected output:
p
y
t
h
o
n

Hint: You can literally write `for letter in "python":` and Python will give 
you each letter one at a time.

# Challenge 2 — Check If a Letter is in a Word

Python has a super useful word called `in` that checks if something is inside 
something else.

Example:
    if "a" in "apple":
        print("Yes!")

Your task:
1. Ask the user to type a letter
2. Check if that letter is in the word "banana"
3. If it is, print "Found it!"
4. If it's not, print "Not in the word."

Expected output:
Enter a letter: a
Found it!

Enter a letter: z
Not in the word.

# Challenge 3 — Build a List of Letters

Your task:
1. Start with an empty list called `guessed`
2. Use a while loop to ask the user for letters one at a time
3. Every letter they type, add it to the `guessed` list using .append()
4. If they type "done", stop the loop and print the full list

Expected output:
Enter a letter (or "done" to quit): a
Enter a letter (or "done" to quit): p
Enter a letter (or "done" to quit): e
Enter a letter (or "done" to quit): done
You guessed: ['a', 'p', 'e']

Hint: Remember .append()? That's how you add stuff to a list.
my_list.append("new item")

# Challenge 4 — Hangman: Starting the Hangman game 🙈

Store a secret word. Print it out as underscores — one underscore for each 
letter in the word.

Expected output:
Secret word: apple
_ _ _ _ _