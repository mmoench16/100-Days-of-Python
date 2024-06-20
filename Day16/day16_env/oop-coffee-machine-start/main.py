from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

def prompt_user_for_choice() -> str:
    """Asks user for choice and returns choice as string."""
    choices = ["espresso", "latte", "cappuccino", "report", "off"]
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice not in choices:
        print("Sorry, I don't recognise that command. Please try again.")
        choice = prompt_user_for_choice()
        
    return choice

machine_on = True

while machine_on:
    choice = prompt_user_for_choice()
    if choice == "off":
        machine_on = False
        continue
    
    if choice == "report":
        coffee_machine.report()
        money_machine.report()
        continue

    choice = menu.find_drink(choice)
    enough_resources = coffee_machine.is_resource_sufficient(choice)

    if enough_resources:
        transaction_successful = money_machine.make_payment(choice.cost)
        if transaction_successful:
            coffee_machine.make_coffee(choice)