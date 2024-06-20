import copy

animals = {
    "lion": ["scary", "big", "cat"],
    "elephant": ["big", "gray", "wrinkled"],
    "teddy": ["cuddly", "stuffed"]
}

# PERFORM A SHALLOW COPY (dictionaries SHARE LIST, copies references)
# things = animals.copy()

# PERFORM A DEEP COPY (each dictionary contains its OWN LIST)
things = copy.deepcopy(animals)
print(id(things["teddy"]), things["teddy"])
print(id(animals["teddy"]), animals["teddy"])

print()

things["teddy"].append("toy")
print(things["teddy"])
print(animals["teddy"])
