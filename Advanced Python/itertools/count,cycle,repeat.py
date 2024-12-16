from itertools import count, cycle, repeat

a = [1,2,3]

for i in count(10):
    print(i)
    if i == 15:
        break
    
sum = 0
for i in cycle(a):
    print(i)
    sum += i
    if sum > 30:
        break
    
for i in repeat(a, 4):  # stops after 4 iterations
    print(i)