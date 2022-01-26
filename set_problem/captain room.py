"""
Problem statement on one note

time constraint
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
# complexity O(m+n)
k = input()
rooms = list(map(int, input().split()))

room_set = set(rooms)

# this iterative operation removes one entry of each no
for r in room_set:
    rooms.remove(r)

# since captain had only one entry, so the diff will remove all entries from room_set except captain's, since rooms
# no longer has captain's room no.
print(*room_set.difference(rooms))
