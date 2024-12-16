from itertools import accumulate
import operator

a = [1,3,5,6]

print(list(accumulate(a)))  # creates a list containing cumulative sum of input iterable
print(list(accumulate(a, func=operator.mul)))   # creates a list containing cumulative product(multiply with previous item) of input iterable

