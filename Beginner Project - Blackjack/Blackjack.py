import art
import random

""" Blackjack Game with terminal interface"""

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
        print(f"Your cards are {user_cards}, and your total score is {user_total}.\n")

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

    # Dealer draw
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

    