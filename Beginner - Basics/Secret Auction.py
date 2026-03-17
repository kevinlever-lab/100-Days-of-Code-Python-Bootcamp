import auction_art
print(auction_art.logo)
""" 
Secret Auction:
A command-line auction application that collects bids from multiple participants
and determines the highest bidder.
A Dictionary is written to and read from
"""
secret_auction = {}
new_bidder = True

while new_bidder:
    # TODO-1: Ask the user for input
    bidder = input("What is your name?\n")
    # TODO-2: Save data into dictionary {name: price}
    amount = int(input("What is your bid?\n"))
    secret_auction[bidder] = amount
    # TODO-3: Whether if new bids need to be added
    other_bids = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if other_bids != 'yes':
        new_bidder = False
    #Clear the screen
    print("\n" * 100)

# TODO-4: Compare bids in dictionary
max_bid = 0
max_bidder = ""
for bidder_name in secret_auction:
    if secret_auction[bidder_name] > max_bid:
        max_bid = secret_auction[bidder_name]
        max_bidder = bidder_name

print(f"The winner is {max_bidder} with a bid of ${max_bid}.\n")

