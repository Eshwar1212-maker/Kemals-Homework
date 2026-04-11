# Challenge 1
name = input("What is your name? ")
number = int(input("What is your favorite number? "))
if number % 2 == 0:
    print(f"{name} picked an even number.")
else:
    print(f"{name} picked an odd number.")

# Challenge 2
name = input("What is your name? ")
lives = int(input("How many lives do you have? "))
if lives > 3:
    print(f"You're doing great {name}.")
elif lives == 3:
    print("Getting low.")
else:
    print("Game over.")

# Challenge 3
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 > num2:
    print(f"{num1} is bigger.")
elif num2 > num1:
    print(f"{num2} is bigger.")
else:
    print("It's a tie.")