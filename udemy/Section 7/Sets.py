farm_animals = {"sheep", "cow", "hen", "goat", "horse"}
print(farm_animals)

more_animals = {'hen', 'sheep', 'horse', 'cow', 'goat'}

if farm_animals == more_animals:
    print("The sets are equal")
else:
    print("The sets are different")
    
print(set("12345"))
print(list("12345"))

Numbers = {} # this evaluates to a dict variable type
Numbers = {*""} # this evaluates to a set variable type

data = ['cow', 'sheep', 'goat', 'hen', 'horse', 'sheep', 'hen']

# To remove duplicates from a list but preserve the order of the items

print(list(dict.fromkeys(data)))
print()
small_ints = set(range(21))
print(small_ints)

small_ints.clear()