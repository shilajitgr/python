"""
Mr. Vincent works in a door mat manufacturing company. One day,
he designed a new door mat with the following specifications:

Mat size must be N x M. ( N is an odd natural number, and M is 3 times N.)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.

Size: 7 x 21
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------

    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------
"""

import math

# Enter your code here. Read input from STDIN. Print output to STDOUT
inp = input()
n = int(inp.split(" ")[0])
m = int(inp.split(" ")[1])  # m = 3 * n
patterns = [".", "|.."]
mid = math.ceil(n / 2)
welcome = "WELCOME".center(m, "-")
pattern_base = []
for i in range(1, mid):
    center_pattern = patterns[0] + (i - 1) * patterns[1]

    pattern_base.append(center_pattern)

for i in range(mid - 1):
    print((pattern_base[i] + "|" + pattern_base[i][::-1]).center(m, "-"))

print(welcome)

for i in range(1, mid):
    print((pattern_base[mid - 1 - i] + "|" + pattern_base[mid - 1 - i][::-1]).center(m, "-"))
