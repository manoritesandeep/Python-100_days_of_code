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

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function 1: check user's guess with actual answer
def check_answer(guess,answer,turns):
    if guess > answer:
        print("Too high.")
        return turns-1
    elif guess < answer:
        print("Too low.")
        return turns-1
    else:
        print(f"You got it right. The answer was {answer}.")

# Function 2: Set difficulty level and monitor the turns
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

# Function 3: Game
def game():
    print(logo)

    #Choosing a random number between 1 and 100.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    ans = r.randint(1,101)
    print(ans)

    num_turns = set_difficulty()

    guess = 0
    while guess != ans:
        print(f"You have {num_turns} turns remaining to guess the number.")
        guess = int(input("Make a guess: "))

        num_turns = check_answer(guess,ans,num_turns)
        if num_turns == 0:
            print("You are out of turns!")
            return
        elif guess != ans:
            print("Guess again!")

game()