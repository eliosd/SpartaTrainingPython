games = {
    "game_title": ["Rust"],
    "genre": "Survival",
    "release_date": "08/02/2018",
    "reviews": {
        "recent": "Very Positive",
        "overall": "Overwhelmingly Positive"
    }
}

print(games, type(games))

print(games["game_title"])  # DICTIONARY NAME [ KEY ]

games["game_title"] = "Rust"
games["genre"] = ["Survival"]

print(games.get("missing_key"))  # Return None

print(games)

print(games.keys())
print(games.values())
print(games.items())

