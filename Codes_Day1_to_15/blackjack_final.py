"""
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
"""

import random as r
from replit import clear
from blackjack_art import logo


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = r.choice(cards)
    return card


def calculate_score(cards: list):
    if sum(cards) == 21 and len(cards) == 2:
        # BlackJack at start
        return 0
    # Change ace to 1 from 11 if sum > 21
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(player_score, computer_score):
    if player_score > 21 and computer_score > 21:
        return "You went over! You lose!"

    if player_score == computer_score:
        return "Its a draw!"
    elif player_score > 21:
        return "You went over! You lose."
    elif computer_score > 21:
        return "You win! Opponent went over."
    elif player_score == 21:
        return "BlackJack! You win!"
    elif computer_score == 21:
        return "You lose! Opponent has BlackJack!"
    elif player_score > computer_score:
        return "You win!"
    else:
        return "You lose."


def play_game():
    print(logo)

    player_cards = []
    computer_cards = []
    is_game_over = False

    # Deal cards
    for _ in range(2):
        player_cards.append(deal_card())
        computer_cards.append(deal_card())
    # print(player_cards)
    # print(computer_cards)

    # User starts
    while not is_game_over:
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Player cards: {player_cards}, current score: {player_score}")
        print(f"Computer first card is: {computer_cards[0]}")

        if player_score == 0 or computer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            user_draw_card = input("Do you want to draw another card? 'y' or 'n': ")
            if user_draw_card == 'y':
                player_cards.append(deal_card())
            else:
                is_game_over = True

    # Computer Plays
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Player final cards: {player_cards}, final score: {player_score}")
    print(f"Computer final cards: {computer_cards}, final score: {computer_score}")
    print(compare(player_score, computer_score))


# Ask if player wants to play again? If yes, run play_game() function
while input("Would you like to play blackjack? Type 'y' or 'n': ") == 'y':
    clear()
    play_game()
