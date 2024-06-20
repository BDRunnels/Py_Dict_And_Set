farm_animals = {'cow', 'sheep', 'hen', 'goat', 'horse'}
# {} -> set or dict (kv pairs) (sets are unordered)
# [] -> list
# () -> tuple
print(farm_animals)

for animal in farm_animals:  # unordered each time
    print(animal)

print()
print("Indexing a sequence")
animals_list = ['cow', 'sheep', 'hen', 'goat', 'horse']
goat = animals_list[3]
print(goat)

# print("Indexing a set is NOT possible")
# goat = farm_animals[3]  # cannot index a set

more_animals = {'sheep', 'goat', 'cow', 'horse', 'hen'}
if more_animals == farm_animals:
    print("The sets are equal")
else:
    print("The sets are NOT equal")
