class Bird:
    def __init__(self, species, colour, can_fly=True):
        self.species = species
        self.colour = colour
        self.wings = 2
        self._age = 0

class Penguin(Bird):
    def __init__(self, subspecies, colour=("Black", "White")):
        super().__init__("Penguin", colour, False)
        self.subspecies = subspecies

    def hunt_for_fish(self):
        print("Splash")

class Emperor(Penguin):
    def __init__(self, location_found="Antarctica"):
        super().__init__("Penguin", ("Black", "White"))
        self.location_found = location_found

penguin = Penguin("Rockhopper")
jimmy = Emperor("London-Zoo")
print(jimmy.location_found)