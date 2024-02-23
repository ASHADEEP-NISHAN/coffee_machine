MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.0
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}
def format_menu_res(odr):
    global water,milk,coffee,cost,r_coffee,r_milk,r_water
    water=int(MENU[odr]["ingredients"]["water"])
    milk=int(MENU[odr]["ingredients"]["milk"])
    coffee=int(MENU[odr]["ingredients"]["coffee"])
    cost=float(MENU[odr]["cost"])
    r_water=int(resources["water"])
    r_milk=int(resources["milk"])
    r_coffee=int(resources["coffee"])
    return water,milk,coffee,cost,r_coffee,r_milk,r_water
def ask_money():
    global total_money
    quarters = int(input("how many quarters? "))
    dimes = int(input("how many dimes? "))
    nickles = int(input("how many nickles? "))
    penny= int(input("how many penny? "))
    total_money=0.25*quarters+0.10*dimes+0.05*nickles+0.01*penny
    return total_money
profit=0
def change_left(odr):
    global profit
    ask_money()
    format_menu_res(odr)
    if total_money > cost:
        change = total_money - cost
        profit=profit+cost
        print(f"here is your {odr}.have a nice day.")
    else:
        change=total_money
        print(f"sorry! insufficient money")
    change=round(change,2)
    return change
def resouce_left(odr):
    format_menu_res(odr)
    if r_water >= water and r_milk >= milk and r_coffee >= coffee:
        l_water = r_water - water
        l_milk= r_milk - milk
        l_coffee=r_coffee-coffee
    else:
        l_water=r_water
        l_milk=r_milk
        l_coffee=r_coffee
        print(f"sorry don't have enough ingredients for {odr}")
        exit()
    resources["water"] = l_water
    resources["milk"]=l_milk
    resources["coffee"]=l_coffee
check=True
while check:
    order = input("“What would you like? (espresso/latte/cappuccino):").lower()
    if order == 'report':
        for key, value in resources.items():
            print(f"{key}:{value}")
        print(f"Total Profit is ${profit}")
    elif order == 'off':
        check=False
    elif order == 'espresso':
        resouce_left(order)
        print(f"here is ${change_left(order)} in change")
    elif order == 'latte':
        resouce_left(order)
        print(f"here is ${change_left(order)} in change")
    elif order == 'cappuccino':
        resouce_left(order)
        print(f"here is ${change_left(order)} in change")
    else:
        print("choose valid option")


