# from module import variable
# print(variable)

# from turtle import Turtle, Screen
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(500)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# from prettytable import PrettyTable
# table = PrettyTable()
# table.add_column("Pokemon", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])

# print(table)

from money_machine import MoneyMachine
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker

money_machine = MoneyMachine()
coffe_maker = CoffeeMaker()
menu = Menu()



is_on = True

while is_on:
    options = menu.get_items()
    choice = input(F"what would you like? ({options}): ")
    if choice == 'off':
        is_on = False
    elif choice == "report":
        coffe_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffe_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost): # type: ignore
            coffe_maker.make_coffee(drink)
            
                
                
            


















