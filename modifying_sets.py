# numbers = {}  # creates empty DICT not SET
numbers = set()
print(numbers, type(numbers))

# a_numbers = {*""}  # create empty SET, DO NOT DO
# print(a_numbers, type(a_numbers))

# numbers.add(1)
# print(numbers)

                # ADDING VALUES
# Getting 4 unique vales (SETS CANNOT CONTAIN DUPLICATE VALUES)
# while len(numbers) < 4:
#     next_value = int(input("Please enter your next value: "))
#     numbers.add(next_value)
# print(numbers)

                # REMOVE DUPLICATE VALUES FROM LIST (move to set())?
data = ["blue", "red", "blue", "green", "red", "blue", "white"]

# Create sorted set from list to remove duplicates
unique_data = sorted(set(data))
print(unique_data)

# Create a list of unique colors, keeping order they appeared
unique_data = list(dict.fromkeys(data))
print(unique_data)

print()
print(dict.fromkeys(data))
