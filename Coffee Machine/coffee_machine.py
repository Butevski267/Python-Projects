MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
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

def report(menu, resources):
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"coffee: {resources['coffee']}g")
    print(f"money: ${resources['money']}")

def choices(answer):
    if answer == 'report':
        report(MENU,resources)
    elif answer == 'latte' or answer == 'espresso' or answer == 'capuccino':
        print("Please insert coins.\n")

def coins(quarters, dimes, nickels, pennies,answer):
    list = ['latte','espresso','cappuccino']
    total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    for item in list:
        if answer == item and total >= MENU[item]['cost']:
            resources['money'] += MENU[item]['cost']
            return round(total - MENU[item]['cost'],2)
        elif total < MENU[item]['cost']:
            print("Insufficient coins.")
            return 0

def check_resources(answer):
    flag = True
    list = ['latte','espresso','cappuccino']
    for item in list:
        if answer == item:
            if resources['water'] < MENU[item]['ingredients']['water']:
                print("Sorry there is not enough water!")
                flag = False
                return flag
            else:
                resources['water'] -= MENU[item]['ingredients']['water']
            if resources['milk'] < MENU[item]['ingredients']['milk']:
                print("Sorry there is not enough milk!")
                flag = False
                return flag
            else:
                resources['milk'] -= MENU[item]['ingredients']['milk']
            if resources['coffee'] < MENU[item]['ingredients']['coffee']:
                print("Sorry there is not enough coffee!\n")
                flag = False
                return flag
            else:
                resources['coffee'] -= MENU[item]['ingredients']['coffee']
                
    return flag
is_running = True

def payment(total_cost,answer):
    list = ['latte','espresso','cappuccino']
    for item in list:
        if total_cost < MENU[item]['cost']:
            print("Sorry that is not enough money. Money refunded.")
        else:
            resources['money'] += (total_cost - MENU[item]['cost'])

while is_running == True:
    answer = input("What would you like? (espresso, latte, capuccino): ")
    choices(answer)

    if answer != 'report':
        flag = check_resources(answer)
        
        if flag == True:
            #choices(answer)
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickels = int(input("How many nickels?: "))
            pennies = int(input("How many pennies?: "))
            total_cost = coins(quarters, dimes, nickels, pennies, answer)
            if total_cost != 0:
                print(f"Here is your {answer} enjoy!")
                print(f"Here is ${total_cost} in change.")
        else:
            print("Please refill the machine!")
            break



