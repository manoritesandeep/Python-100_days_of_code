#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from guess_the_number_art import logo
import random as r

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

NUMBER_OF_GUESSES_EASY = 10
NUMBER_OF_GUESSES_HARD = 5

user_choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
random_number = r.choice(range(1,101))
print(random_number)

game_on = True
if user_choice == 'easy':
    while NUMBER_OF_GUESSES_EASY > 0 and game_on:
        print(f"You have {NUMBER_OF_GUESSES_EASY} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))

        if user_guess == random_number:
            print(f"You guessed the correct number. The number was {random_number}.")
            game_on = False
        elif user_guess > random_number:            
            print("Too High.")
        else:
            print("Too low.")
        NUMBER_OF_GUESSES_EASY -=1
elif user_choice == 'hard':
    while NUMBER_OF_GUESSES_HARD > 0 and game_on:
        print(f"You have {NUMBER_OF_GUESSES_HARD} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))

        if user_guess == random_number:
            print(f"You guessed the correct number. The number was {random_number}.")
            game_on = False
        elif user_guess > random_number:            
            print("Too High.")
        else:
            print("Too low.")
        NUMBER_OF_GUESSES_HARD -=1
else:
    print("You entered a wrong choice!")