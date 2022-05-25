class Mammal:
    def __init__(self, name):
        self.name = name

    def give_birth(self):
        print("Giving birth to live young.")


class Platypus(Mammal):
    def __init__(self):
        super().__init__("Platypus")

    def give_birth(self):
        print("Laying eggs...")

mam = Mammal("Mammal")
mam.give_birth()

perry = Platypus()
perry.give_birth()