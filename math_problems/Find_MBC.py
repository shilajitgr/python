"""
right triangle ABC is given, its right angle is joined to middle of hypotenuse by line BM.

Now we need to find angle MBD
"""

import math

AB = float(input())
BC = float(input())

# hypotenuse mid point theorem states that length of the line joining right angle to middle of hypotenuse is equal to half of the length of hypotenuse, so MBC becomes an isoceles triangle, thereby making angle theta and ACB equal, so here we will find angle ACB which is equal to MBC
angle = math.degrees(math.atan(AB/BC))

print(f'{int(round(angle))}{chr(176)}', sep='')
