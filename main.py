from itertools import filterfalse
QUARTERS = 0.25
DIMES = 0.10
NICKLES = 0.05
PENNIES = 0.01

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 12,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 22,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 20,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0,
}

"""This functions take coffee type as an input and returns a list [water, milk, coffee, cost] """
def get_recipe (coffee_type):
    water = MENU.get(coffee_type).get("ingredients").get("water")

    milk = MENU.get(coffee_type).get("ingredients").get("milk")

    coffee =  MENU.get(coffee_type).get("ingredients").get("coffee")

    cost = MENU.get(coffee_type).get("cost")

    return int(water) ,int(milk), int(coffee), float(cost)


def check_resources (w,m,c):
    if w > resources.get("water"):
        print("Sorry there is no enough water.")
        return False
    elif m > resources.get("milk"):
        print("Sorry there is no enough milk.")
        return False
    elif c > resources.get("coffee"):
        print("Sorry there is no enough coffee.")
        return False
    else:
        return True


def process_coins(coffee):
    print("Please insert Money.")
    riyals = float(input("how many riyals?:")) * 1
    fives = float(input("how many five riyals?: ")) * 5
    tens = float(input("how many tens?:")) * 10

    total = riyals + fives + tens

    coffee_cost = float(MENU.get(coffee).get("cost"))
    if total >= coffee_cost:
        print(f"Here is SR{round((total - coffee_cost),2)} in change.")
        print(f"Here is your {coffee} ☕. Enjoy!")

    else:
        print("Sorry that's not enough money. Money refunded.")






should_continue = True

while should_continue:
    user_choice= input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice == "latte" or user_choice == "cappuccino" or user_choice == "espresso":

        # check_resources(w, m, c):

        water = MENU.get(user_choice).get("ingredients").get("water")

        milk = MENU.get(user_choice).get("ingredients").get("milk")

        coffee = MENU.get(user_choice).get("ingredients").get("coffee")

        cost = MENU.get(user_choice).get("cost")


        if check_resources(water ,milk,coffee):
            print("Hello we preparing your coffee")
            process_coins(user_choice)

            resources["water"] = int(resources.get("water") - water)
            resources["milk"] = int(resources.get("milk") - milk)
            resources["coffee"] = int(resources.get("coffee") - coffee)
            resources["money"] += float(cost)
        else:
            should_continue = False

    elif user_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee:{resources['coffee']}g")
        print(f"Money: SR{resources['money']}")

    elif user_choice == "off":
        exit(0)
    else:
        print("invalid input")





