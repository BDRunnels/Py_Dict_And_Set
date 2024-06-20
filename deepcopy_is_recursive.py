from challenge import dCopy
import copy

original = {
    "Tim": ["Buchalka", ["Programmer", "Teacher"]],
    "J-P": ["Roberts", ["Programmer", "Teacher"]],
}

copy_1 = copy.deepcopy(original) # deep copy of all contained objects
copy_2 = dCopy(original) # only goes 1 level down to copy (shallow). It references list in `original`.

original["Tim"].append("Australia")
original["J-P"].append("UK")

# SAME THING (append a new job to inner list - 2nd item)
original["Tim"][1].append("Cashier")
jp_list = original["J-P"]
jp_list[1].append("Courier")

print(original)
print(copy_1)
print(copy_2)
