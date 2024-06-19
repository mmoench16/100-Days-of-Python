MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

credit = 0.0

QUARTER = 0.25
DIME = 0.10
NICKLE = 0.05
PENNY = 0.01

machine_on = True

def prompt_user_for_choice() -> str:
    """Asks user for choice and returns choice as string."""
    choices = ["espresso", "latte", "cappuccino", "report", "off"]
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice not in choices:
        print("Sorry, I don't recognise that command. Please try again.")
        choice = prompt_user_for_choice()
        
    return choice

def print_report(resources, credit):
    """Prints a report of the currently available resources."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${credit}")

def check_resources(resources, menu, choice):
    """Takes current resources, the menu and choice and inputs and returns true or false whether resources are sufficient."""
    ingredients = menu[choice]["ingredients"]
    for ingredient in ingredients:
        if resources[ingredient] < ingredients[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
        
    return True

def process_coins():
    """Processes the coins inserted."""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    return (quarters * QUARTER) + (dimes * DIME) + (nickles * NICKLE) + (pennies * PENNY)

def check_transaction(amount, choice, menu, credit):
    """Takes inserted coins as an input and determines whether enough money has been provided."""
    cost = menu[choice]["cost"]

    if amount < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False, 0.0
    elif amount > cost:
        change = round(amount-cost, 2)
        credit += cost
        print(f"Here is ${change} dollars in change.")

    return True, credit

def make_coffee(choice, resources, menu):
    """Makes the coffee, i.e. deducts the resources and returns the beverage."""
    ingredients = menu[choice]["ingredients"]
    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]

    return resources 

while machine_on:
    choice = prompt_user_for_choice()
    print(f"Choice: {choice}")
    if choice == "off":
        machine_on = False
        continue
    
    if choice == "report":
        print_report(resources, credit)
        continue

    enouch_resources = check_resources(resources, MENU, choice)
    if enouch_resources:
        amount = process_coins()
        transaction_successful , credit = check_transaction(amount, choice, MENU, credit)[0:2]
        if transaction_successful:
            resources = make_coffee(choice, resources, MENU)