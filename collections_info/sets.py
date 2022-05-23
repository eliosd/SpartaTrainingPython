#  SETS are unordered and unique
marvelchar = {"Iron Man", "Thor", "Captain America", "Hulk"}

print(marvelchar, type(marvelchar))

marvelchar.add("Spider-Man")
marvelchar.add("Black Widow")

print(marvelchar)

marvelchar.discard("Iron Man")
print(marvelchar)


#  Frozen Set - immutable
