trial_1 = {"Bob", "Charley", "Georgia", "John"}
trial_2 = {"Anne", "Charley", "Eddie", "Georgia"}

check_set = trial_1.intersection(trial_2)  # common elements in BOTH sets
print(check_set)

# Sets of animals
farm_animals = {"sheep", "hen", "cow", "horse", "goat"}
wild_animals = {"lion", "elephant", "tiger", "goat", "panther", "horse"}

# animals that can be rode
potential_rides = {"donkey", "horse", "camel"}

intersection = farm_animals & wild_animals & potential_rides
print(intersection)  # only horse appears in all 3 sets

mounts = farm_animals.intersection(wild_animals, potential_rides)  # SAME AS '&'
print(mounts)
