from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

"""  
Coffee Machine 

A command-line coffee machine simulator that manages a menu, resources,
and payments for making espresso, latte, and cappuccino.

Process:
    1. Initializes the menu, coffee maker, and money machine from their
       respective modules.
    2. Displays the available menu items and their ingredients at startup.
    3. Prints an initial report of the coffee machine's resources and profit.
    4. Repeatedly prompts the user to select a drink until the machine is
       turned off, with the following commands available:
        - 'off':       Shuts down the coffee machine and exits the program.
        - 'report':    Displays the current machine resources and total profit.
        - drink name:  Processes an order for the requested drink by:
            a. Verifying the drink exists on the menu.
            b. Checking if sufficient resources are available to make the drink.
            c. Displaying the drink's ingredients and resource requirements.
            d. Processing the customer's payment.
            e. Deducting the required resources and making the coffee.

Functions:
    drink_ingredients(order_name): Searches the menu for a drink by name and
                                   displays its cost and ingredient requirements
                                   (water, milk, and coffee amounts).

Dependencies:
    menu.Menu:                Provides the drink menu, item lookup via
                              find_drink(), and lists available drinks
                              via get_items().
    coffee_maker.CoffeeMaker: Manages machine resources, checks resource
                              availability via is_resource_sufficient(), makes
                              coffee via make_coffee(), and prints a resource
                              report via report().
    money_machine.MoneyMachine: Handles payment processing via make_payment(),
                                tracks profit, and prints a financial report
                                via report().
"""

# Print Menu items to confirm access
# Create menu object from the class first
cafe_menu = Menu()
# Use method to get menu items
menu_items = cafe_menu.get_items()
print("Menu Items")
print(f"{menu_items}\n")

# My method to extract coffee cost and ingredients
def drink_ingredients(order_name):
    """Search for a drink by name and extract the ingredients. Similar to find_drink() method but includes ingredients"""
    for item in cafe_menu.menu:
        if item.name == order_name:
            print(f"Name: {item.name}")
            print(f"Cost: {item.cost}")
            print("Order ingredients:")
            #The following loop statement work but going with individual print statements for now
            # for ingredient, amount in item.ingredients.items():
            #     print(f"    {ingredient}: {amount}")
            # print("")
            print(f"Water: {item.ingredients["water"]}ml")
            print(f"Milk: {item.ingredients["milk"]}ml")
            print(f"Coffee: {item.ingredients["coffee"]}g")

# Print coffee machine report to confirm access
# Create coffee machine object from the class first
print(f"Coffee Machine Report: ")
cafe_coffeemaker = CoffeeMaker()
cafe_coffeemaker.report()
print("")

# Report the amount of money in the coffee machine
cafe_money_machine = MoneyMachine()
# Report the current profit
print(f"Current coffee machine profit: ")
cafe_money_machine.report()
print("")

is_on = True

while is_on:
    drink = input("What would you like? (espresso/latte/cappuccino): ")
    # Switch the coffee machine off
    if drink == "off":
        is_on = False
    # Print coffee machine report
    elif drink == "report":
        print(f"Coffee Machine Report: ")
        cafe_coffeemaker.report()
        # Print total amount of money received
        print(f"Coffee machine profit: ")
        cafe_money_machine.report()
    else:
        # Try to find a drink if it is in the menu
        drink_order = cafe_menu.find_drink(drink)
        # Check if the object is None before printing. (None means drink is not in the menu)
        if drink_order is not None:
            print(f"Your {drink_order.name} is in the menu")
            # Check if sufficient resources to make a cup of coffee
            machine_resources = cafe_coffeemaker.is_resource_sufficient(drink_order)
            # Check if enough resources before printing
            if machine_resources:
                # Retrieve the ingredients for the coffee selected
                print(f"Your drink resource requirements are: ")
                drink_ingredients(drink_order.name)
                print(f"We can make your {drink_order.name}!")
                # Ask for payment
                # make_payment takes cost as input, and calls process_coins() which asks user for payment
                # make_payment then checks if sufficient funds were inserted
                drink_price = drink_order.cost
                payment_received = cafe_money_machine.make_payment(drink_price)
                # Update coffee machine resources after payment and making the coffee
                cafe_coffeemaker.make_coffee(drink_order)
