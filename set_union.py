#####
# farm_animals = {"sheep", "hen", "cow", "horse", "goat"}
# wild_animals = {"lion", "elephant", "tiger", "goat", "panther", "horse"}
#
# # UNION - doesn't matter which way you do it (a + b = b + a)
# all_animals_1 = farm_animals.union(wild_animals)
# print(all_animals_1)
#
# all_animals_2 = wild_animals.union(farm_animals)
# print(all_animals_2)
#
# all_animals_3 = wild_animals | farm_animals
# print(all_animals_3)
######
from prescription_data import adverse_interactions

meds_to_watch = set()

# for interaction in adverse_interactions:
#
#     #  SAME
#     # meds_to_watch = meds_to_watch.union(interaction)
#     # meds_to_watch = meds_to_watch | interaction
#     # BUT MORE EFFICIENT (not creating a new set each time
#     # meds_to_watch.update(interaction)
#     meds_to_watch |= interaction

meds_to_watch.update(*adverse_interactions)  # * UNPACKS, instead of looping (above)

print(sorted(meds_to_watch))  # returns a list
print(*sorted(meds_to_watch), sep="\n")
