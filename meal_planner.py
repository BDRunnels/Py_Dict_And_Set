from smart_fridge import pantry, recipes

# Confirm data is available
# print(pantry)
# print(recipes)

# Comprehension (more advanced)
# display_dict = {str(index + 1): meal for index, meal in enumerate(recipes)}
# print(display_dict)


def add_shopping_item(data: dict, item: str, amount: int) -> None:
    """
    Add a dictionary containing `item` and `amount` to `data` list
    """
    data[item] = data.setdefault(item, 0) + amount


display_dict = {}
for index, key in enumerate(recipes):
    # enumerate is used with any iterable and returns an index for us
    display_dict[str(index + 1)] = key # convert index to str for user input

shopping_list = {}
while True:
    # Display menu of recipes we know how to cook
    print("Please choose a recipe:")
    print("-" * 25)
    for key, value in display_dict.items():
        print(f"{key} - {value}")

    choice = input(": ")

    if choice == "0":
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"You have selected {selected_item}")
        print("checking ingredients...")
        ingredients = recipes[selected_item]
        print(ingredients)
        for food_item, required_qty in ingredients.items():
            qty_in_pantry = pantry.get(food_item, 0) # 0 is default value is key does not exist
            if required_qty <= qty_in_pantry:
                print(f"\t{food_item} OK")
            else:
                qty_to_buy = required_qty - qty_in_pantry
                print(f"\tYou need to buy {qty_to_buy} of {food_item} to make {selected_item}")
                add_shopping_item(shopping_list, food_item, qty_to_buy)

for things in shopping_list.items():
    print(things)
