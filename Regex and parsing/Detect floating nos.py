"""
Input Format

The first line contains an integer N, the number of test cases.
The next N line(s) contains a string .

Output Format

Output True or False for each test case.

Sample Input 0

    4
    4.0O0
    -1.00
    +4.54
    SomeRandomStuff

Sample Output 0

    False
    True
    True
    False


Explanation 0
    4.0O0:  O is not a digit.
    -1.00: is valid.
    +4.54: is valid.
    SomeRandomStuff: is not a number.
"""

import re

pattern = r'^[+-.]?([0-9])*[\.][0-9]+$'
for num in range(int(input())):
    val = input()
    if re.match(pattern, val):
        print(True)
    else:
        print(False)