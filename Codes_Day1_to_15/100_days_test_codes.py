# name = str(input("Enter a name: "))
# print(name)


# h = input("height: ")
# w = input("weight: ")

# bmi = int(w) / (float(h)*float(h))
# print(int(bmi))

# print(int(2.7))


# print('aabc'.count('a'))
# print('Mary had a little lamb'.count('a'))

## Randomisation
# import random as r
# print(f"{r.randint(0,100)}")

# ls = list(range(0,100))
# print(f"Random number choice: {r.choice(ls)}")

# import random as r
# random_num = r.choice(list(range(0,100)))
# print(random_num)
# # Take this random number and check for prime:
# for i in range(2,random_num):
#     if random_num%i == 0:
#         print(f"{random_num} is not a prime number.")
#         break
# else:
#     print(f"{random_num} is a prime number.")


# Caesar Cipher
## Encode
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# text = 'abc'
# shift = 3
# cipher_text = ""
# # plain_text = "hello"
# for letter in text:
#     position = alphabet.index(letter)
#     # print(position)
#     new_position = shift + position
#     # print(new_position)
#     new_text = alphabet[new_position]
#     # print(new_text)
#     cipher_text += new_text
# print(cipher_text)

## Decode
# text = 'def'
# shift = 3
# decipher_text = ""
# for letter in text:
#     position = alphabet.index(letter)
#     # print(position)
#     new_position = position - shift
#     # print(new_position)
#     new_text = alphabet[new_position]
#     # print(new_text)
#     decipher_text += new_text
# print(decipher_text)


## Secret Auction Programs

# b = {"Angela": 123, "James": 321}

# highest_bid = 0
# winner = ""
# for bidder in b:
#     bid_amount = b[bidder]
#     if bid_amount > highest_bid:
#         highest_bid = bid_amount
#         winner = bidder
# print(f"The winner is {winner} with a bid of ${highest_bid}")

# calculator
# if operation_symbol == "+":
#     answer = add(num1,num2)
# elif operation_symbol == "-":
#     answer = subtract(num1,num2)
# elif operation_symbol == "*":
#     answer = multiply(num1,num2)
# elif operation_symbol == "/":
#     answer = divide(num1,num2)
# elif operation_symbol == "^":
#     answer = square(num1)
# else:
#     print("Select a valid operator for your operations: ")


# a,b,c = 1,2,3
# print(a,b,c)

# d,f= input("Enter two number for d and f, respectively: ").split(" ")
# print(f"D: {d} F: {f}") # Enter two number for d and f, respectively: 4 5 Ouput-> D: 4 F: 5


### BlackJack ###
# import random as r
# def draw_cards():
#     cards_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     card = r.choice(cards_deck)
#     return card

# player_cards = [draw_cards() for _ in range(2)]
# # print(f"Your cards: {player_cards}")
# print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")


# user_cards = [draw_cards() for _ in range(2)]
# computer_cards = [draw_cards() for _ in range(2)]
# print(user_cards)
# print(computer_cards)
# user_cards = []
# computer_cards = []
# for _ in range(2):
#     user_cards.append(draw_cards())
#     computer_cards.append(draw_cards())
#     print(user_cards)
#     print(computer_cards)

# cards = [11,2,5,6,7]
# if 11 in cards:
#     cards.remove(11)
#     cards.append(1)
#     print(cards)


## Custom logo generator
# http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20

# Guess the number
# import random as r
# random_number = r.choice(range(1,101))
# print(random_number)



