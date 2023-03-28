############### Blackjack #####################
############### Our Blackjack House Rules #####################

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
from blackjack_art import logo
# deck_suits = ["Hearts","Club","Spade","Diamond"]
# deck_numbers = list(range(1,14))
# card = str(r.choice(deck_numbers)) + "of" + str(r.choice(deck_suits))
# print(card) 




# print("Do you want to play a game of blackjack? Type 'y' or 'n': ").lower()

# player_name = input("Enter your name: ")

# Draw cards:
def draw_cards():
    cards_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = r.choice(cards_deck)
    return card

# # print("Type 'y' to get another card, type 'n' to pass: ")
# if input("Type 'y' to get another card, type 'n' to pass: ").lower() == 'y':
#     player_cards.append(r.choice(cards_deck))
#     print(f"Computer's first card: {computer_cards}")
#     # print(f"Computer's first card: {computer_cards}")
#     # computer_cards.append(r.choice(cards_deck))
#     # print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")

# if sum(player_cards) > 21:
#     print("You went over. You lose.") 


def check_total(player_total,player_cards,computer_cards):
    if player_total >21:
        print(f"You final hand: {player_cards}, final score: {player_total}")
        print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")

def blackjack():
    print(logo)
    player_cards = [draw_cards() for _ in range(2)]
    player_total = sum(player_cards)
    print(f"Your cards: {player_cards}, current score: {player_total}")

    computer_cards = draw_cards()
    print(f"Computer's first card: {computer_cards}")

    should_continue = True
    while should_continue:
        if input("Type 'y' to get another card, type 'n' to pass: ").lower() == 'y':
            player_cards = player_cards.append(draw_cards())
            player_total = sum(player_cards)
            print(f"Your cards: {player_cards}, current score: {player_total}")
            print(f"Computer's first card: {computer_cards}")
        
        if check_total(player_total,player_cards,computer_cards) == True:
            print("You went over. You lose 😭")
            should_continue = False
        else:            
            print("Do you want to play a game of blackjack? Type 'y' or 'n': ")#.lower()

blackjack()            













