a = [1, 2, 3, 4, 5]
b = map(lambda x: x*2, a)
print(list(b))

b = [x*2 for x in a]    # performs the same operation as map
print(b)

c = filter(lambda x: x%2 == 0, a)
print(list(c)) # prints all even nums

from functools import reduce

prod = reduce(lambda x, y: x*y, a)

"""
For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5). 
If initial is present, it is placed before the items of the iterable in the calculation, 
and serves as a default when the iterable is empty.
"""

print(prod) # prints the product of all elements in a