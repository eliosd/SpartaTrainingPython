class Move:
    def __init__(self, name, type, power):
        self.name = name
        self.type = type
        self.power = power

if __name__ == "__main__":
    flamethrower = Move(
        name="Flamethrower",
        type="Fire",
        power=100
    )

    print(flamethrower)