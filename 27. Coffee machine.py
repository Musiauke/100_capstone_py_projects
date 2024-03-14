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
    "money": 0
}


coins = {
    "Penny": 0.01,
    "Nickel": 0.05,
    "Dime": 0.10,
    "Quarter": 0.25
}


def what_coins():
    print("Please insert coins.")
    pennys = int(input("How many pennies (0.01 $)?: "))
    nickels = int(input("How many nickels (0.05 $)?: "))
    dimes = int(input("How many dimes (0.10 $)?: "))
    quarters = int(input("How many quarters (0.25 $)?: "))
    inserted_coins = pennys * coins["Penny"] + nickels * coins["Nickel"] + dimes * coins["Dime"] + quarters * coins["Quarter"]
    return inserted_coins
    

def order_implication(order, inserted_coins):
    for ingredient in MENU[order]["ingredients"]:
        if resources[ingredient] < MENU[order]["ingredients"][ingredient]:
            print(f"Sorry, there is not enough {ingredient}.")
            return False

    for ingredient in MENU[order]["ingredients"]:
        resources[ingredient] -= MENU[order]["ingredients"][ingredient]

    resources["money"] += inserted_coins - MENU[order]["cost"]

    return True


def order():
    while True:
        user_choice = input("What would you like to choose? Espresso (e), cappuccino (c) or latte (l)? ").lower()

        if user_choice == 'c':
            chosen_order = "cappuccino"
        elif user_choice == 'e':
            chosen_order = 'espresso'
        elif user_choice == 'l':
            chosen_order = 'latte'
        elif user_choice == 'report':
            print(resources)
            continue
        else:
            print("Incorrect input, try again.")
            continue  

        return chosen_order  

def main():
    print("Welcome to the coffee machine!\n")
    while True:
        chosen_order = order()
        if chosen_order:
            print(f"You have chosen {chosen_order}.")
            inserted_coins = what_coins()
            is_it_enough = order_implication(chosen_order, inserted_coins)

            if is_it_enough:
                print("Here is your drink! Enjoy!")
            else:
                print("Transaction failed.")
        else:
            print("Incorrect input. Please try again.")

        if input("Would you like to order another coffee? (y/n): ").lower() != 'y':
            print("Thank you for using the coffee machine. Goodbye!")
            break

if __name__ == '__main__':
    main()
