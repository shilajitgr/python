"""
problem statement:

https://www.hackerrank.com/challenges/py-check-subset/problem?isFullScreen=true
"""

for _ in range(int(input())):
    Alen = int(input())
    A = set(map(int, input().split()))
    Blen = int(input())
    B = set(map(int, input().split()))
    if A - B:   # if this is null that means A is subset of B, but in such a scenario else block will be executed
        print(False)
    else:
        print(True)
