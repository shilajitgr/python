"""
Problem statement on one note

time constraint
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
# complexity O(m+n)
k = input()
rooms = list(map(int, input().split()))

room_set = set(rooms)

for r in room_set:
    rooms.remove(r)

print(*room_set.difference(rooms))