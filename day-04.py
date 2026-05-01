# day-04.py
# number guessing game

import random

# Computer picks a random number between 1 and 100
secret = random.randint(1, 100)
attempts = 0

print("I'm thinking of a number between 1 and 100.")
print("Try to guess it!")

while True:
    guess = int(input("Your guess:"))
    attempts = attempts + 1

    if guess < secret:
        print("Higher! Try a bigger number.")
    elif guess > secret:
            print("Lower! Try a smaller number.")
    else:
         print("Correct! You got it in", attempts, "attempts.") 
         break       