import pokemon
from move import Move

class Charmander(pokemon.Pokemon):
    def __init__(self):
        super().__init__(
            name="Charmander",
            type="Fire",
            hp=7,
            attack=9,
            defence=5
        )
        self.moves.append(Move("Scratch", "Normal", 10))
        self.moves.append(Move("Growl", "Normal", 0))

    def use_move(self, move_name) -> (int, str):
        for move in self.moves:
            if move_name == move.name:
                print(f"{self.name} used {move_name}!")
                return move.power + self.attack, move.type

class Pikachu(pokemon.Pokemon):
    def __init__(self):
        super().__init__(
            "Pikachu", "Electric",
            hp=6,
            attack=6,
            defence=6
            )
        self.moves.append(Move("Thundershock", "Electric", 20))
        self.moves.append(Move("Tail Whip", "Normal", 0))


char = Charmander()
# print(char.type)
# print(char.hp)

for move in char.moves:
    print(f"{move.name} ({move.type}): {move.power}")

result = char.use_move("Scratch")
print(result)