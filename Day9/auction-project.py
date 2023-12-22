from os import system

bids = {}
bidding_finished = False


def find_highest_bid(bidding_record):
    higest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > higest_bid:
            higest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid amount of {higest_bid}")


while not bidding_finished:
    name = input("What's your name?\n")
    bid_price = int(input("What is your bid:\n$"))
    bids[name] = bid_price
    others = input("Are there any other bidders? Type 'yes' or 'no'\n")
    if others == "no":
        bidding_finished = True
        find_highest_bid(bids)
    elif others == "yes":
        system("clear")
