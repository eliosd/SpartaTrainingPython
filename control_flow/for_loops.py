# alphabet = ["A", "B", "C", "D", "E"]
#
# for letter in alphabet:
#     print("The letter is: ")
#     print(letter.lower())
#     if letter == "d":
#         print("Oh no, not d!")
#     else:
#         print("Hoorahh!")
#
#
# # Iterating through sub-lists
#
# nest = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
#
# for sublist in nest:
#     print(sublist)
#     for number in sublist:
#         print(number)


games = {
    "game_title": ["Rust"],
    "genre": "Survival",
    "release_date": "08/02/2018",
    "reviews": {
        "recent": "Very Positive",
        "overall": "Overwhelmingly Positive"
    }
}

# for count in games:
#     print(games[count])

# for count in games.values():
#     print(count)



# Unpack into tuple

# for key, value in games.items():
#     print(f"The {key} is {value}")


r = range(5)
print(type(r))

for i in range(5):
    print(f"This is line number: {i + 1}")

for x in enumerate(games):
    print(f"Key number {i} is {key}")