from data import Menu, resources


# create a function to ask user how many coins of different types
def coins(user_req, coffee_price):
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    paid = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    if paid > coffee_price:
        money_return = (paid - coffee_price)
        print(f"here is ${round(money_return, 5)} change")
        return f"Here is your {user_req}, Enjoy!"
    elif paid < coffee_price:
        return f"not enough money to buy {user_req}"
    else:
        return f"Here is your {user_req}, Enjoy!"


milk = int(resources['milk'])
water = int(resources['water'])
coffee = int(resources['coffee'])


def resource_check(milk_req, coffee_req, water_req):
    if milk >= milk_req and water >= water_req and coffee >= coffee_req:
        return 1
    else:
        return 0


money = 0
coffee_rate = 0
game = True
while game:
    # take input from the user
    user_input = input("What would you like? (espresso/latte/cappuccino):").lower()

    if user_input == "espresso":
        coffee_rate = float(Menu["espresso"]["cost"])
        milk_espresso = 0
        water_espresso = int(Menu["espresso"]["ingredient"]["water"])
        coffee_espresso = int(Menu["espresso"]["ingredient"]["coffee"])
        resource_check(milk_espresso, coffee_espresso, water_espresso)
        if resource_check(milk_espresso, coffee_espresso, water_espresso) == 1:
            milk -= milk_espresso
            water -= water_espresso
            coffee -= coffee_espresso
            money += coffee_rate
            print(coins(user_input, coffee_rate))
        else:
            print("Sorry there is not enough resources")
    elif user_input == "latte":
        coffee_rate = float(Menu["latte"]["cost"])
        milk_latte = int(Menu["latte"]["ingredient"]["milk"])
        water_latte = int(Menu["latte"]["ingredient"]["water"])
        coffee_latte = int(Menu["latte"]["ingredient"]["coffee"])
        if resource_check(milk_latte, coffee_latte, water_latte) == 1:
            milk -= milk_latte
            water -= water_latte
            coffee -= coffee_latte
            money += coffee_rate
            print(coins(user_input, coffee_rate))
        else:
            print("Sorry there is not enough resources")

    elif user_input == "cappuccino":
        coffee_rate = float(Menu["cappuccino"]["cost"])
        milk_cappuccino = int(Menu["cappuccino"]["ingredient"]["milk"])
        water_cappuccino = int(Menu["cappuccino"]["ingredient"]["water"])
        coffee_cappuccino = int(Menu["cappuccino"]["ingredient"]["coffee"])
        if resource_check(milk_cappuccino, coffee_cappuccino, water_cappuccino) == 1:
            milk -= milk_cappuccino
            water -= water_cappuccino
            coffee -= coffee_cappuccino
            money += coffee_rate
            print(coins(user_input, coffee_rate))
        else:
            print("Sorry there is not enough resources")

    elif user_input == "report":
        print(f"milk: {milk}\nwater: {water}\ncoffee: {coffee}\nmoney: ${money}")
    elif user_input == 'off':
        game = False
        print("Machine is stopped")
    else:
        print("Enter a valid input")
        game = True


