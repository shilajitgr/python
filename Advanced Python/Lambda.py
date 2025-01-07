add10 = lambda x: x + 10

# this is equivalent to 
def add10_func(x):
    return x + 10

print(add10(5))

mult = lambda x, y: x * y

print(mult(2, 7))

points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D)
# the default behavior of sorted is to sort by the first element of the tuple
print(points2D_sorted)

# the following code will modify the behavior of sorted to sort by the 
# second element of the tuple
points2D_sorted = sorted(points2D, key=lambda x: x[1])
print(points2D_sorted)

points2D_sorted = sorted(points2D, key=lambda x: x[0] + x[1])
print(points2D_sorted)