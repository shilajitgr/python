from collections import deque

d = deque()

d.append(1)
d.append(2)
d.appendleft(4)

print(d)

print(d.pop())

print(d.popleft())
d.clear()

d.extend([2,5,1,6])
d.extendleft([6,4])
print(d)

d.rotate(2)
print(d)
d.rotate(-3)
print(d)