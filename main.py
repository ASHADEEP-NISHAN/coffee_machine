from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
money_machine=MoneyMachine()
coffee_maker=CoffeeMaker
is_on=True

while is_on:
    options=Menu.get_items()
    choice=input(f"what would you like ? ({options})")
    if choice =="off":
        is_on=False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink=Menu.find_drink(choice)
        coffee_maker.is_resource_sufficient(drink)