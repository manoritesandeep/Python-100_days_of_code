rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
game_images = [rock,paper,scissors]
user_input = int(input("Type 0 for 'Rock', 1 for 'Paper', 2 for 'Scissors': "))
if user_input >=3 or user_input<0:
    print("Invalid number, you lose!")
else:
    print(game_images[user_input])

    comp_input = random.randint(0,2)
    print("Computer chose:")
    print(game_images[comp_input])

    # Rock 0, Paper 1, Scissors 2
    if user_input==0 and comp_input==2: 
        print("You Win!")
    elif comp_input==0 and user_input==2: 
        print("You lose!")
    elif user_input >=3 or user_input<0:
        print("Invalid number, you lose!")
    elif comp_input > user_input:
        print("You lose!")
    elif user_input > comp_input:
        print("You win!")
    elif user_input== comp_input: 
        print("It's a draw!")