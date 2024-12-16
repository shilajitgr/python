from itertools import permutations, combinations

a = [1,3,4,]

perm = permutations(a, 2)
print(list(perm))

comb = combinations(a, 2)   
print(list(comb))