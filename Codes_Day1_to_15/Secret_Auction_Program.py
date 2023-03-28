from replit import clear
# call clear() to clear the output in the console.
from Secret_auction_prog_art import logo

# bidders = []
# def bid_entries(bidder_names, amount_bid):
#     bids = {}
#     bids["Name"] = bidder_names
#     bids['Amount'] = amount_bid
#     bidders.append(bids)

bids ={}
def find_highest_bidder(bidding_records):
    # b = {"Chan": 1234, "Jenny": 4321}
    highest_bid = 0
    winner = ""
    for bidder in bidding_records:
        bid_amount = bidding_records[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner of this bid is {winner} with a bid of ${highest_bid}")

print(logo)

more_bidders = True
while more_bidders:
    print("Welcome to the secret auction program.")
    bidder_name = input("What is your name?: ")
    bid_amt = float(input("What's your bid?: $"))
    # bid_entries()
    # Name is key, Value is price
    bids[bidder_name] = bid_amt

    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n ").lower()
    if should_continue == "no":
        more_bidders = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()

# bid_entries(bidder_names = bidder_name, 
#             amount_bid = bid_amt)
# print(bidders)