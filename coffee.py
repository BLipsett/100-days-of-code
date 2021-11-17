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
  supply = (MENU[user_choice]["ingredients"])
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

  if user_choice == "latte": 
    print("take a " + user_choice)
    checkSource(user_choice)
  else:
    print("please make a choice from the list")
    start_Order()


start_Order()
#TODO check resources to make drink type 
# checkSource(coffee)

#TODO reply with cost 

#TODO check user