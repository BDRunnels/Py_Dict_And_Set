data = [
    ("orange", "a sweet, orange, citrus fruit"),
    ("apple", "good for making cider"),
    ("lemon", "a sour, yellow citus fruit"),
    ("grape", "a small, sweet fruit growing in bunches"),
    ("melon", "sweet and juicy"),
]

# ord() returns Unicode code point for a one-character string.
# print(ord("a"))
# print(ord("b"))
# print(ord("z"))


def simple_hash(s: str) -> int:
    """A ridiculously simple hashing function"""
    basic_hash = ord(s[0])
    return basic_hash % 10


# # BUILT-IN HASH FUNCTION
# for key, value in data:
#     j = hash(key)
#     print(key, j)

def get(k: str) -> str:
    """return a value for a key or None if key does not exist"""
    hash_code = simple_hash(k)
    if values[hash_code]:
        return values[hash_code]
    else:
        return None


keys = [""] * 10  # ["", "", "",...]
values = keys.copy()

for key, value in data:
    h = simple_hash(key)
    print(f"{key} : {h}")
    keys[h] = key
    values[h] = value

print(keys)
print(values)
print()

value = get("banana")
print(value)
