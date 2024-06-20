animals = {
    "lion": ["scary", "big", "cat"],
    "elephant": ["big", "gray", "wrinkled"],
    "teddy": ["cuddly", "stuffed"]
}

things = animals.copy()
# animals["teddy"] = "toy"
print(things["teddy"])  # "cuddly"
print(animals["teddy"])  # "toy"

print(id(things))
print(id(animals))

print()

things["teddy"].append("toy")
print(things["teddy"])
print(animals["teddy"])
