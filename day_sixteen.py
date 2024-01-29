from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine




money_machine = MoneyMachine()
cofee_maker = CoffeeMaker()
menu = Menu()

is_on = True 

while is_on:
    options = menu.get_items()
    user_order = input(f"What would you like to drink? ({options}: ")
    if user_order == 'off':
        is_on == False
        
    elif user_order == 'report':
        cofee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_order)
        if cofee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            cofee_maker.make_coffee(drink)

