recipe = {
        "chicken": ["black", 100],
        "potatoes": {"size": "small", "count": 2},
        "salt": set(["pink", 1]),
        "malt vinegar": 2,
        "coriander": "fresh",
    }

def deepcopy(data: dict|list) -> dict:
    copy = {}
    for item, value in data.items():
        if isinstance(value, (dict, list, set)):
            copy[item] = value.copy()
        else:
            copy[item] = value
        
    return copy


recipe_2 = deepcopy(recipe)
recipe["chicken"].append("5")
recipe["coriander"] = "farm fresh"
recipe["malt vinegar"] = 3
recipe["salt"].add(5)
recipe["potatoes"].update({"count": 5}) 
print(recipe["chicken"])
print(recipe_2["chicken"])
print()
print(recipe["potatoes"])
print(recipe_2["potatoes"])
print()
print(recipe["salt"])
print(recipe_2["salt"])
print()
print(recipe["malt vinegar"])
print(recipe_2["malt vinegar"])
print()
print(recipe["coriander"])
print(recipe_2["coriander"])

