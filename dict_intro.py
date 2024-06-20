vehicles = {
    "dream": "Honda 250T",
    "er5": "Kawasake ER5",
    "can-am": "Bombardier Can-Am 250",
    "virago": "Yamaha XV250",
    "tenere": "Yamaha XT 650",
    "jimny": "Suzuki Jimny 1.5",
    "fiesta": "Ford Fiesta Ghia 1.4",
    "roadster": "Triumph Street Triple"
}

my_car = vehicles["fiesta"]
print(my_car)

commuter = vehicles["virago"]
print(commuter)

learner = vehicles.get("er5")
print(learner)

# for key in vehicles:
#     print("{} : {}".format(key, vehicles[key]))

# ADDING ITEMS TO DICTIONARY (no add method exists)
vehicles["starfighter"] = "Lockheed F-104"
vehicles["learjet"] = "Bombardier Learjet 75"
vehicles["toy"] = "glider"

# UPGRADE Virago
vehicles["virago"] = "Yamaha XV535"

# DELETING item
del vehicles["starfighter"]
# del vehicles["f1"]
result = vehicles.pop("f1", "You wish! Sell the Learjet")
print(result)
plane = vehicles.pop("learjet")
print(plane)

bike = vehicles.pop("tenere", "Not present")
print(bike)
print()

for key, value in vehicles.items(): # PREFERRED LOOP for DICTIONARIES
    print(key, value, sep=", ")
