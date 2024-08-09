from menu import MENU

resources = {
    "water": 1000,
    "milk": 500,
    "coffee": 300,
    "chocolate": 100,
    "ice_cream": 200,
    "whiskey": 100,
    "sugar": 50,
    "cream": 100,
    "money": 0,
}

def check_resources(drink_choice, resources):
    for ingredient, amount in MENU[drink_choice]['ingredients'].items():
        if amount > resources.get(ingredient, 0):
            print(f"🚨 Sorry, there is not enough {ingredient}.")
            return False
    return True

def calculate_coins():
    print("💰 Please insert coins.")
    try:
        quarters = int(input("🪙 How many quarters?: "))
        dimes = int(input("🪙 How many dimes?: "))
        nickels = int(input("🪙 How many nickels?: "))
        pennies = int(input("🪙 How many pennies?: "))
    except ValueError:
        print("❌ Invalid input. Please enter numbers only.")
        return 0
    total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    return total

def process_transaction(cost, payment):
    if payment >= cost:
        change = round(payment - cost, 2)
        if change > 0:
            print(f"💵 Here is your change: ${change}")
        resources['money'] += cost
        return True
    else:
        print("❌ Sorry, that's not enough money. Money refunded.")
        return False

def make_coffee(drink_choice):
    for ingredient, amount in MENU[drink_choice]['ingredients'].items():
        resources[ingredient] -= amount
    print(f"☕ Here is your {drink_choice}! Enjoy!")

start_machine = True
while start_machine:
    print("🔧 Type 'report' to view current resources or 'off' to turn off the machine.")
    drink_choice = input("📋 What would you like? (espresso/latte/cappuccino/mocha/americano/irish coffee): ").lower()

    if drink_choice == "off":
        start_machine = False
        print("🔌 Turning off the machine. Goodbye!")
    elif drink_choice == "report":
        print("📊 Current Resources:")
        print(f"💧 Water: {resources['water']}ml")
        print(f"🥛 Milk: {resources['milk']}ml")
        print(f"☕ Coffee: {resources['coffee']}g")
        print(f"🍫 Chocolate: {resources.get('chocolate', 0)}g")
        print(f"🍨 Ice Cream: {resources.get('ice_cream', 0)}g")
        print(f"🥃 Whiskey: {resources.get('whiskey', 0)}ml")
        print(f"🍬 Sugar: {resources.get('sugar', 0)}g")
        print(f"🍶 Cream: {resources.get('cream', 0)}ml")
        print(f"💵 Money: ${resources['money']}")
    elif drink_choice in MENU:
        if check_resources(drink_choice, resources):
            payment = calculate_coins()
            if process_transaction(MENU[drink_choice]['cost'], payment):
                make_coffee(drink_choice)
        else:
            continue
    else:
        print("❗ Invalid option. Please choose a valid coffee option.")