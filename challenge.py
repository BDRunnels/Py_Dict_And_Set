from smart_fridge import recipes


def dCopy(d: dict) -> dict:
    """
    Copy a dictionary, creating copies of `list` or `dict` values
    Function will crash with an AttributeError if values aren't
    lists or dicts.
    :param d: dictionary to copy
    :return: A copy of `d`, with values being copies of original value
    """
    new_dict = {}
    for k, v in d.items():
        new_v = v.copy()
        new_dict[k] = new_v

    return new_dict


recipes_copy = dCopy(recipes)
recipes_copy["Butter chicken"]["ginger"] = 300
print(recipes_copy["Butter chicken"]["ginger"])
print(recipes["Butter chicken"]["ginger"])
