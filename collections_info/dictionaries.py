# Dictionaries

data_eng_37 = {
    "course_name": "Data Engineering 37",
    "client": "Home Office",
    "trainer": {
        "name": "David Harvey",
        "energy_levels": "low"
    }
}

print(data_eng_37, type(data_eng_37))

print(data_eng_37["client"])  # DICTIONARY NAME [ KEY ]

data_eng_37["trainer"] = "David Harvey"
data_eng_37["trainees"] = ["Elios", "John"]

print(data_eng_37["trainer"]["energy_levels"])

print(data_eng_37.get("missing_key"))  # Return None

print(data_eng_37)


