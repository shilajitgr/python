"""
Input Format
The first line contains a, the second line contains b, and the third line contains m.

Task
You are given three integers: a, b, and m. Print two lines.
On the first line, print the result of pow(a,b). On the second line, print the result of pow(a,b,m).

Example:
    input-
    3
    4
    5

    output-
    81
    1
"""

import math

a, b, m = int(input()), int(input()), int(input())
power = int(math.pow(a, b))
print(power)
print(power % m)  # print(math.pow(a,b,m)) would give the same result
