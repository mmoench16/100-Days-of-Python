from art import logo
import os

clear = lambda: os.system('clear')

print(logo)

auction_active = True
bids = {}

def determine_highest_bid():
    highest_bid = 0
    winner = ""

    for name in bids:
        if bids[name] > highest_bid:
            highest_bid = bids[name]
            winner = name
    
    print(f"The winner of the auction is {winner} with {highest_bid}$.")

while auction_active:
    name = input("What is your name? ")
    bid = input("What is your bid ($)? ")
    bids[name] = int(bid)

    additional_bidders = input("Are there any more bidders? Type 'yes' or 'no'. ")

    if additional_bidders == 'no':
        auction_active = False
    else:
        clear()

determine_highest_bid()