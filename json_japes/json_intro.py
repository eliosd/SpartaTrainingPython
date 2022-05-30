import json

# car_data = {
#     "make": "Tesla",
#     "type": "Electric",
#     "faults": 4,
#     "death_trap": True,
#     "driver": None
# }

# dumps = json.dumps(car_data)
#
# with open('tesla.json', 'w') as jsonfile:
#     json.dump(car_data, jsonfile)

with open("spartan.json") as jsonfile:
    spartan = json.load(jsonfile)

print(spartan)