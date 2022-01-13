"""
.remove(x)
This operation removes element  from the set.
If element  does not exist, it raises a KeyError.
The .remove(x) operation returns None.

Example:
    # >>> s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
    # >>> s.remove(5)
    # >>> print s
    # set([1, 2, 3, 4, 6, 7, 8, 9])
    # >>> print s.remove(4)
    # None
    # >>> print s
    # set([1, 2, 3, 6, 7, 8, 9])
    # >>> s.remove(0)
    # KeyError: 0

.discard(x)
This operation also removes element  from the set.
If element  does not exist, it does not raise a KeyError.
The .discard(x) operation returns None.

Example:
    # >>> s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
    # >>> s.discard(5)
    # >>> print s
    # set([1, 2, 3, 4, 6, 7, 8, 9])
    # >>> print s.discard(4)
    # None
    # >>> print s
    # set([1, 2, 3, 6, 7, 8, 9])
    # >>> s.discard(0)
    # >>> print s
    # set([1, 2, 3, 6, 7, 8, 9])

.pop()
This operation removes and return an arbitrary element from the set.
If there are no elements to remove, it raises a KeyError.

Example:

    # >>> s = set([1])
    # >>> print s.pop()
    # 1
    # >>> print s
    # set([])
    # >>> print s.pop()
    # KeyError: pop from an empty set
"""

n = int(input())
s = set(map(int, input().split()))

add = sum(s)
for _ in range(int(input())):
    cmd = input().split(" ")
    if cmd[0] == "pop":
        if s:
            add -= s.pop()
    else:
        val = int(cmd[1])
        if cmd[0] == "remove" and val in s:
            s.remove(val)
            add -= val
        else:
            if val in s:
                s.discard(val)
                add -= val

print(add)
