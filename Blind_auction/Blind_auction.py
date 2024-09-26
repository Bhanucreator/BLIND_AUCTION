import art
print(art.logo)
def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    # Find the highest bid and the winner
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

def start_bidding():
    bids = {}
    continue_bidding = True
    while continue_bidding:
        name = input("What is your name?: ")
        price = int(input("What's your bid?: $"))
        bids[name] = price

        should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
        if should_continue == "no":
            continue_bidding = False
            # Once all bidders are done, we call the function to find the highest bidder
            find_highest_bidder(bids)
        elif should_continue == "yes":
            print("\n" * 20)  # Clears the screen for privacy

# To start the bidding process, call the function
start_bidding()
