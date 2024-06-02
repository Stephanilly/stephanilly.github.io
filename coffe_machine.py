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
    "water": 500,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


# TODO 3. Check resources are sufficient to make drink order
def check_resources(order):
    resources_needed = MENU[order]["ingredients"]
    # print(resources_needed)
    for item_needed in resources_needed:
        # print(item_needed)
        # print(resources[item_needed])
        if resources[item_needed] <= resources_needed[item_needed]:
            print(f"Sorry there isn't enough {item_needed}.")
            return False
    return True
    # print(item_needed, resources_needed[item_needed])


# TODO 4. Process coins
def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters: "))*.25
    dimes = int(input("How many dimes: "))*.1
    nickels = int(input("How many nickels: "))*.05
    pennies = int(input("How many pennies: "))*.01
    amt_paid = quarters + dimes + nickels + pennies
    return amt_paid


# TODO 5. Make coffee & deduct resources
def consume_resources(order):
    resources_needed = MENU[order]["ingredients"]
    for item_needed in resources_needed:
        resources[item_needed] -= resources_needed[item_needed]
    return f"Here is your {order}. ☕ Enjoy!"


# TODO 2. Prompt user for order
machine_on = True
while machine_on:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # TODO 1. Print a report of all the coffee machine resources
    if order == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${"%.2f" % resources['money']}")
    # TODO 6. Turn off machine
    elif order == "off":
        machine_on = False
    else:
        # print(MENU[order])
        cost = MENU[order]["cost"]
        if check_resources(order):
            print(f"Total cost is ${"%.2f" % cost}")
            # TODO 4.5 Check that the transaction was successful / provide change
            paid = process_coins()
            if paid > cost:
                change = paid - cost
                print(f"Here is ${"%.2f" % change} in change.")
                resources["money"] += cost
                print(consume_resources(order))
            elif paid == cost:
                resources["money"] += cost
                print(consume_resources(order))
            else:
                print("Sorry, that's not enough money. Money refunded.")
