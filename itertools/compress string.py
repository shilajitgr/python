"""
Sample Input

1222311
Sample Output

(1, 1) (3, 2) (1, 3) (2, 1)
Explanation

First, the character  occurs only once. It is replaced by (1,1).
Then the character 2 occurs three times, and it is replaced by (3, 2)
and so on.

----------Elegant solution-------------

from itertools import groupby
s=map(int,list(raw_input()))
l=[(sum(1 for i in g),k) for k,g in groupby(s)]
print ' '.join(map(str,l))
"""


from itertools import groupby

s = list(input())
# groups = list(groupby(s))
idx = 0
output = []
for g in groupby(s):
    # [f(x) if condition else g(x) for x in sequence]
    count = 0
    for i in s[idx:]:
        if g[0] == i:
            count += 1
            idx += 1
        else:
            break

    output.append((count, int(g[0])))

print(*output, sep=" ")
