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

def deal_cards():
    cards_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = r.choice(cards_deck)
    return card

def calculate_score(cards:list):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards)> 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
#Bug fix. If you and the computer are both over, you lose.
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"

    if computer_score ==  user_score:
         return "Its a draw!"
    elif computer_score == 0:
        return "You lose, opponent had a blackjack!"
    elif user_score == 0:
        return "You win! You have a blackjack!"
    elif user_score >21:
        return "You went over 21. You lose!"
    elif computer_score >21:
        return "You win! Computer went over 21."
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"    

def play_game():
    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    # user_cards = [deal_cards() for _ in range(2)]
    # computer_cards = [deal_cards() for _ in range(2)]

    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())
        # print(user_cards)
        # print(computer_cards)

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score>21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_cards())
            else:
                is_game_over = True

    while computer_score !=0 and computer_score <17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)
    
    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")=='y':
    clear()
    play_game()


        