import art
import random

"""
Blackjack Game

A command-line Blackjack card game played against a computer dealer.

Process:
    1. Deals two cards each to the player and dealer at the start of each round.
    2. Prompts the player to draw additional cards ('y') or hold ('n').
    3. Ends the player's turn automatically if:
        - A Blackjack is dealt (Ace + 10-value card = 21 in 2 cards).
        - The player's score exceeds 21 (bust).
    4. Dealer draws cards automatically until reaching a score of 17 or higher.
    5. Compares final scores and announces the result.
    6. Prompts the player to start a new game or quit after each round.

Functions:
    draw_card():                Returns a randomly drawn card value from a
                                standard deck, where face cards are worth 10
                                and Aces start at 11.
    calculate_score(cards):     Calculates and returns the total score of a
                                hand, adjusting Aces from 11 to 1 if the total
                                exceeds 21, and returning 0 for Blackjack.
    compare_score(u_score,
                  d_score):     Compares the player's score against the
                                dealer's score and returns the result as
                                a string.
    start_game():               Initializes and runs a single round of
                                Blackjack, managing the game loop, player
                                input, dealer logic, and final score display.
"""

def draw_card():
    """Returns a random number from the list of cards in the list"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10 ]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Return the score calculated from the list of cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare_score(u_score, d_score):
    """Compares the user score u_score against the computer/dealer score d_score."""
    if u_score == d_score:
        return "Scores are equal. Draw!!"
    elif u_score == 0:
        return "You win with Blackjack!"
    elif d_score == 0:
        return "The dealer wins with Blackjack!"
    elif u_score > 21:
        return "Your score is greater than 21. Dealer Wins!"
    elif d_score > 21:
        return "The dealer's score is greater than 21. You Win!"
    elif u_score < d_score:
        return "Dealer has a higher score. Dealer Wins!"
    else:
        return "You have a higher score. You Win!"

def start_game():
    print(art.logo)
    user_total = -1
    dealer_total = -1
    user_cards = []
    dealer_cards = []
    is_game_on = True


    for draw in range(2):
        user_cards.append(draw_card())
        dealer_cards.append(draw_card())

    print(f"The dealer's first card is {dealer_cards[0]}.\n")

    while is_game_on:
        user_total = calculate_score(user_cards)
        dealer_total = calculate_score(dealer_cards)
        print(f"Your cards are {user_cards}, and your total score is {21 if user_total == 0 else user_total}.\n")

        #Check for Black Jack or user bust
        if user_total == 0 or dealer_total == 0 or user_total > 21:
            is_game_on = False
        else:
            # User draw
            user_draw = str(input("Would you like to draw another card? Type 'y' for yes and 'n' for no!: \n"))
            if user_draw.lower() == "n":
                is_game_on = False
            elif user_draw.lower() == "y":
                user_cards.append(draw_card())
                user_total = calculate_score(user_cards)
            else:
                print("Invalid input. Please type 'y' or 'n'")
                is_game_on = False

    # Dealer draw only if user has not busted
    if user_total <= 21:
        while dealer_total != 0 and dealer_total < 17:
            dealer_cards.append(draw_card())
            dealer_total = calculate_score(dealer_cards)


    # Compare scores
    print(compare_score(user_total, dealer_total))
    # Print the final scores
    print(f"Your final cards are {user_cards}, and your total score is {21 if user_total == 0 else user_total}.\n")
    print(f"Dealer cards are {dealer_cards}, and the dealer's total score is {21 if dealer_total == 0 else dealer_total}.\n")

while input("Do you wish to play Blackjack? Type 'y' for yes and 'n' for no: ") == 'y':
    print("\n" * 20)
    start_game()

    