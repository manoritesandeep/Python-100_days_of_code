############### Blackjack #####################
########## Our Blackjack House Rules ##########
## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
################################################

import random as r
from replit import clear
from blackjack_art import logo

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = r.choice(cards)
    return card

def calculate_score(cards:list):
    if sum(cards) == 21 and len(cards)==2:
        # It's a BlackJack
        return 0
    
    # Check for Ace: Use 1 if sum over 21 else 11
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(player_score, computer_score):
    if player_score >21 and computer_score >21:
        return "Score over 21. You lose!"
    
    if computer_score == player_score:
        return "It's a draw."
    elif computer_score == 0:
        return "You lose. Opponent hit a BlackJack."
    elif player_score == 0:
        return "You got a BlackJack! You win!"
    elif player_score > 21:
        return "You went over. You lose."
    elif computer_score > 21:
        return "You win! Opponent went over."
    elif player_score > computer_score:
        return "You win!"
    else:
        return "You lose."

def play_game():
    print(logo)
    
    # create cards lists
    player_cards = []
    computer_cards = []
    is_game_over = False

    # deal 2 cards each
    for _ in range(2):
        player_cards.append(deal_card())
        computer_cards.append(deal_card())
    # print(player_cards)
    # print(computer_cards)

    while not is_game_over:
        # calculate scores and user plays
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {player_cards}, current score:{player_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if player_score == 0 or computer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            deal_user = input("Do you want to draw another card? 'y' or 'n': ")
            if deal_user == 'y':
                player_cards.append(deal_card())
            else:
                is_game_over = True

    # computer plays
    while computer_score != 0 or computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Print final outcomes
    print(f"Player final cards: {player_cards}, final score: {player_score}")
    print(f"Computer final cards: {computer_cards}, final score: {computer_score}")
    print(compare(player_score, computer_score))

# ask if user wants to play again? clear screen and start over! 
while input("Do you want to play a game of BlackJack? Type 'y' or 'n': ") == 'y':
    clear()
    play_game()