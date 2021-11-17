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
  print(user_Choice)
  


#TODO ask user for drink order

def start_Order():
  user_choice = input("What would you like? (espresso/latte/cappuccino):")
  print("you chose " + user_choice)

  if user_choice != "espressso" or "latte" or "cappuccino": 
    print("please make a choice from the list")
  else:
    print("take a " + user_choice)
    # start_Order()


start_Order()
#TODO check resources to make drink type 
# checkSource(coffee)

#TODO reply with cost 

#TODO check user