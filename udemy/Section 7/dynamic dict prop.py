recipe = {
        "chicken": 100,
        "potatoes": 3,
        "salt": 1,
        "malt vinegar": 5,
    }

values_list = recipe.values()
keys_list = recipe.keys()
item_list = recipe.items()

print(values_list, keys_list, item_list, sep="\n")

recipe["onion"] = 2

print("\n\n")
print(values_list, keys_list, item_list, sep="\n")