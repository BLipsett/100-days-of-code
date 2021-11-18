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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def check_source(drink):
    for item in drink:
        if not resources[item] >= drink[item]:
            print(f"not enough {item}")
            return False
    return True
    
        

def payment(drink):
    total = 0
    total += int(input("how many quarters?")) * .25
    total += int(input("how many dimes?")) * .10
    total += int(input("how many nickels?")) * .05
    print(total)
    if total >= drink:
        change = round(total - drink, 2)
        print(f'{change} is your change')
        global profit
        profit += drink
        return True
    else:
        print('please add more money or select off')
        payment(drink)
    
    

def checkSource(user_Choice):
  supply = (MENU[user_Choice]["ingredients"])

  if supply["water"] >= resources["water"]:
      print("not enough water")
  elif supply["coffee"] >= resources["coffee"]:
      print("not enough coffee")
  elif supply["milk"] >= resources["milk"]:
      print("not enough milk")
  else:
      print("drink can be made")
      deplete_resource(user_Choice)

def deplete_resource(user_choice):
  supply = (user_choice["ingredients"])

  if str(user_choice) == "espresso":
    resources["water"] -= supply["water"]
    resources["coffee"] -= supply["coffee"]
  else: 
    resources["water"] -= supply["water"]
    resources["milk"] -= supply["milk"]
    resources["coffee"] -= supply["coffee"]
  print(resources)


#TODO ask user for drink order
latte = "latte"
espress = "espresso"
cap = "cappuccino"

def start_Order():
  user_choice = input("What would you like? (espresso/latte/cappuccino):")
  print("you chose " + user_choice)

  if user_choice == "latte" or "espresso" or "cappucino": 
    print("take a " + user_choice)
    checkSource(user_choice)
  else:
    print("please make a choice from the list")
    start_Order()
  checkSource(user_choice)


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino)")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"There is {resources['water']}ml of water")
        print(f"There is {resources['milk']}ml of milk")
        print(f"There is {resources['coffee']}ml of coffee")
        print(profit)
    else:
        drink = MENU[choice]
        if check_source(drink['ingredients']):
            if payment(drink['cost']):
                deplete_resource(drink)
#TODO check resources to make drink type 
# checkSource(coffee)

#TODO reply with cost 

#TODO check user