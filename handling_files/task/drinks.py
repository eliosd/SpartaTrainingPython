with open('drinks_menu.txt') as f, open('drinks_orders.txt', 'a') as orders:
    drink = input("What drink would you like: ")
    if drink.lower() in f.read():
        orders.write(drink + "\n")
    else:
        print("Sorry the drink is not on the menu.")
