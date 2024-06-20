d = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    "iv": "four"
}

pantry_items = ['chicken', 'spam', 'egg', 'bread', 'lemon']

# FROM KEYS method
new_dict = dict.fromkeys(pantry_items, 0)
print(new_dict)

# KEYS method (produces a view of dict's keys, can't add or remove keys)
keys = d.keys()
print(keys)

for item in d.keys():
    print(item)

# UPDATE method (update one dict with contents from another)
    # dict keys are UNIQUE
d2 = {
    7: "lucky seven",
    10: "ten",
    3: "this is the new three",
}

# d.update(d2)
# for key, value in d.items():
#     print(key, value)
#
# print()
#
# d.update(enumerate(pantry_items))
# for key, value in d.items():
#     print(key, value)

# VALUES method - returns a view of the dict's values
v = d.values()
print(f"v = {v}")

d[10] = "ten"
print(v)

print("four" in v)  # boolean
print("eleven" in v)  # boolean

    # convert keys and values to list
keys = list(d.keys())
values = list(v)  # => list(d.values())
if "four" in values:
    index = values.index("four")
    key = keys[index]
    print(f"{d[key]} was found with key {key}")

print()

for k, v in d.items():
    if v == "four":
        print(f"{d[k]} was found with key {k}")
