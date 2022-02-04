"""
start() & end()
These expressions return the indices of the start and end of the substring matched by the group.

Code

# >>> import re
# >>> m = re.search(r'\d+','1234')
# >>> m.end()
# 4
# >>> m.start()
# 0

Task
You are given a string S.
Your task is to find the indices of the start and end of string k in S.

Input Format

The first line contains the string S.
The second line contains the string k.

Output Format

Print the tuple in this format: (start _index, end _index).
If no match is found, print (-1, -1).
"""

import re

string = input().strip()
search = input()

regex = re.compile(r"<(\s*[^ ]+\s*)[^>]*>|</(\s*[^ ]+\s*)[^>]*>|<(\s*[^ ])+\s*/>", re.IGNORECASE)

m = re.finditer(r'(?=(%s))' % search, string)
# this gives the start of each overlapping matching entry

iterated = False
for i in m:
    print(f"({i.start()}, {i.end()+len(search)-1})")
    iterated = True

if not iterated:
    print("(-1, -1)")