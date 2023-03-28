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
profit = 0


def is_resources_sufficient(order_ingredients):
    """
    Returns True when order can be made,
    Returns False if ingredients are insufficient
    """
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """
    Takes in coins (quarter, dimes, nickels and pennies) and
    Returns the total calculated from the coins inserted
    """
    print("Please insert coins: ")
    total = int(input("Number of quarters?: ")) * 0.25
    total += int(input("Number of dimes?: ")) * 0.10
    total += int(input("Number of nickels?: ")) * 0.05
    total += int(input("Number of pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_inserted, drink_price):
    """
    Returns True when payment is accepted,
    Returns False if insufficient money is inserted.
    """
    if money_inserted > drink_price:
        change = round(money_inserted - drink_price, 2)
        print(f"Change return: ${change}")
        global profit
        profit += drink_price
        return True
    else:
        print("Not enough money inserted. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """
    Deducts the required ingredients from the available resources.
    """
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Enjoy your {drink_name}")


is_on = True

while is_on:
    user_choice = input("Enter your choice: (espresso/latte/cappuccino): ").lower()

    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        print(f"Water available: {resources['water']} ml.")
        print(f"Milk available: {resources['milk']} ml.")
        print(f"Coffee available: {resources['coffee']} g.")
        print(f"Profit: ${profit}.")
    else:
        drink = MENU[user_choice]
        # print(drink)
        if is_resources_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(user_choice, drink['ingredients'])
