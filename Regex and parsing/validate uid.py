import re

"""
A valid UID must follow the rules below:

It must contain at least 2 uppercase English alphabet characters. [done]
It must contain at least 3 digits (0 - 9). [done]
It should only contain alphanumeric characters (0 - 9, a - z & A - Z). [done]
No character should repeat.
There must be exactly 10 characters in a valid UID. - [done]
"""

for _ in range(int(input())):

    uid = input()
    i = 0
    m = re.match(r"^[A-Z\d]{10}$", uid, re.IGNORECASE)
    if not m:
        print("Invalid")
        continue

    m = re.findall(r"\d", uid)
    if len(m) < 3:
        print("Invalid")
        continue

    m = re.findall(r"[A-Z]", uid)
    if len(m) < 2:
        print("Invalid")
        continue

    uid_set = set(list(uid))
    if len(uid_set) != len(uid):
        print("Invalid")
        continue
    print("Valid")

"""
2
BC1D102354
B1CDEF2354
"""