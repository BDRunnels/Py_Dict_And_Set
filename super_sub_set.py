animals = {"Turtle",
           "Horse",
           "Robin",
           "Python",
           "Swallow",
           "Hedgehog",
           "Wren",
           "Aardvark",
           "Cat",
           }
birds = {"Robin",
         "Swallow",
         "Wren"
         }

# SUPERSET / SUBSET
print(f"birds is a SUBSET of animals: {birds.issubset(animals)}")
print(f"animals is a SUPERSET of birds: {animals.issuperset(birds)}")

print(f"birds is a SUPERSET of animals: {birds.issuperset(animals)}")

print(birds <= animals)
print(birds < animals)
print(animals >= birds)
print(animals > birds)

print("*" * 80)

garden_birds = {"Swallow", "Wren", "Robin"}
print(garden_birds == birds)
print(garden_birds <= birds)
print(garden_birds < birds)  # FALSE (checks proper subset, but isn't same set)

print("*" * 80)

more_birds = {"Wren", "Budgie", "Swallow"}
print(garden_birds >= more_birds)
