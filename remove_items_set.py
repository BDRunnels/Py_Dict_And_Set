small_ints = set(range(21))
print(small_ints)

# small_ints.clear()
# print(small_ints)  # empty set

                # 1)
small_ints.discard(10)
small_ints.remove(11)  # throws exception when trying to remove a NON-existing item
print(small_ints)

small_ints.discard(99)
print(small_ints)

small_ints.remove(99)
print(small_ints)

        ###### DISCARD METHOD ######
# See packing_list.py
        ###### REMOVE METHOD #######
# See prescription_data.py & prescription_trial.py
        ###### POP METHOD ######
# Pops an arbitrary item from the set and returns the item.
# See prescription_processing.py
