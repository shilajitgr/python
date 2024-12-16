from collections import namedtuple

point = namedtuple("Point", "x,y")
pt = point(1,"c")
print(pt.count(5))
print(pt.x, pt.y)