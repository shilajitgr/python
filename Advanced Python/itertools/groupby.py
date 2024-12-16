from itertools import groupby


def smaller_than_5(x):
    return x<5

a = [2,4,5,6]

group_obj = groupby(a, key=smaller_than_5)

for key, value in group_obj:
    print(key, list(value))
    
persons = [
    {"name": "John", "age": 25},
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Carol", "age": 30}
]

group_persons = groupby(persons, key=lambda x: x['age'])    # creates groupby object with persons of the same age in the same group

for key, value in group_persons:
    print(key, *value)