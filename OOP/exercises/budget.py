class Budget:
    def __init__(self, food, clothing, entertainment, transport, housing):
        self.food = food
        self.clothing = clothing
        self.entertainment = entertainment
        self.transport = transport
        self.housing = housing

    def __repr__(self):
        return f"Budget(food={self.food}," \
               f"clothing={self.clothing}," \
               f"entertainment={self.entertainment}," \
               f"transport={self.transport}," \
               f"housing={self.housing})"

    def __str__(self):
        return f"({self.food}, {self.clothing}, {self.entertainment}, {self.transport}, {self.housing})"

    def total_balance(self):
        total = self.food + self.clothing + self.entertainment + self.transport + self.housing
        return total

    def get_food_balance(self):
        return self.food

    def get_clothing_balance(self):
        return self.clothing

    def get_ent_balance(self):
        return self.entertainment

    def get_transport_balance(self):
        return self.transport

    def get_housing_balance(self):
        return self.housing

def deposit(category, amount):
    dep = category + amount
    return dep, f"You have successfully deposited: {amount}"

def withdraw(category, amount):
    wd = category - amount
    if wd < 0:
        return "You do not have the funds to complete this!"
    else:
        return wd, f"You have successfully withdrawn: {amount}"

def transfer(amount, category1, category2):
    tr = category1 - amount
    tr = category2 + amount
    return tr, f"You have successfully transferred: {amount}"


elios = Budget(100, 200, 50, 25, 350)
print(f"Food: {elios.get_food_balance()}")
print(f"Clothing: {elios.get_clothing_balance()}")
print(f"Entertainment: {elios.get_ent_balance()}")
print(f"Transport: {elios.get_transport_balance()}")
print(f"Housing: {elios.get_housing_balance()}")

print(f"Total Balance: {elios.total_balance()}")

print()

print(f"Your total balance for FOOD is: ", deposit(elios.get_food_balance(), 100))

print(f"Your total balance for FOOD is: ", withdraw(elios.get_food_balance(), 50))

print(f"Your total balance for CLOTHING is: ", transfer(10, elios.get_food_balance(), elios.get_clothing_balance()))

print(Budget.__qualname__)