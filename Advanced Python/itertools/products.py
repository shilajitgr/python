from itertools import product

a = [1,4]
b = [2,6]

prod = product(a,b, repeat=2)   
# repeat = 2 means that for the same component iterables a, b, two separate 
# cartesian products will be calculated and then they will be crossed

print(list(prod))