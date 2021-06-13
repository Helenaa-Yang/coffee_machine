from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine  = MoneyMachine()


is_on = True

while is_on:
  option = menu.get_items()
  choice = input(f"​What would you like? ({option}): ")
  if choice == "off":
    is_on = False
  elif choice == "report":
    coffee_maker.report()
    money_machine.report()
  else:
    drink = menu.find_drink(choice)
    sufficient = coffee_maker.is_resource_sufficient(drink)
    payment = money_machine.make_payment(drink.cost)
    if sufficient and payment:
      coffee_maker.make_coffee(drink)
  


# payment = money_machine.make_payment(drink) 會出事XD

# Traceback (most recent call last):
#   File "main.py", line 23, in <module>
#     payment = money_machine.make_payment(drink)
#   File "/home/runner/oop-coffee-machine-start/money_machine.py", line 30, in make_payment
#     if self.money_received >= cost:
# TypeError: '>=' not supported between instances of 'float' and 'MenuItem'
