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
    "water": 3000,
    "milk": 2000,
    "coffee": 1000,
}

def suff_res(ingredients):

    """Checks whether there are enough resources left to process the user's request."""

    is_enough = True
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f"Sorry not enough {item}.")
            is_enough = False
    return is_enough


money = 0
machine_on = True


def process_coins():

    """Returns the total value of the coins inserted."""

    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    
    """Checks whether the user has entered sufficient money or not."""

    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here's your change: ${change}")
        global money
        money += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")

def make_coffee(drink_name, ingredients):
    
    """Makes the coffee, and adjusts the resources accordingly."""

    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink_name}.")


while machine_on:
    choice = input("What would you like? (espresso/latte/cappucino)").lower()
    
    if choice == "off":
        machine_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}")        
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: {money}")       
    else:
        drink = MENU[choice]
        if suff_res(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
