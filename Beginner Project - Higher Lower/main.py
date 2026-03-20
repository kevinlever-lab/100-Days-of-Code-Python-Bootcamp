import art
from game_data import data
from random import choice

"""The user has to guess which celebrity / organisation / platform has the most followers. Game data is stored in a file."""
user_count = 0
end_of_game = False

# Format the dictionary entry into a readable string
def format_data(dict_item, ab_selection):
    name = dict_item["name"]
    # followers = dict_item["follower_count"]
    description = dict_item["description"]
    country = dict_item["country"]
    return f"Compare {ab_selection}: {name}, {description}, from {country}"

def compare_followers(a_num, b_num, user_selection):
        if a_num > b_num: # A has more followers than B
            return user_selection == 'a' # Return true if a > b and user selected a
        else:
            return user_selection == 'b' # Return true if a < b and user selected b

# Select a randon entry from the dictionary
# game_data.data is a list of dictionaries
B_data = choice(data)

while not end_of_game:
    # Position B data is moved to position A. Get new data for B
    A_data =  B_data
    B_data = choice(data)

    # ensure the same item isn't selected twice
    while A_data == B_data:
        B_data = choice(data)

    print(art.logo)
    print(format_data(A_data, "A"))
    # print(A_followers) # Print to check results
    print(art.vs)
    print(format_data(B_data, "B"))
    # print(B_followers) # Print to check results
    # Include an exception
    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    print(user_choice)
    if user_choice != 'a' and user_choice != 'b':
        print("That is not a valid input. Please select 'A' or 'B'")
        end_of_game = True
    else:
        A_followers = A_data["follower_count"]
        B_followers = B_data["follower_count"]

        user_result = compare_followers(A_followers, B_followers, user_choice)
        if user_result:
            user_count += 1
            print(f"That is correct. Current score: {user_count}")
        else:
            print(f"Sorry that was wrong. Final score: {user_count}")
            end_of_game = True




