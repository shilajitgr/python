"""
problem statement:

https://www.hackerrank.com/challenges/py-check-subset/problem?isFullScreen=true
"""

for _ in range(int(input())):
    Alen = int(input())
    A = set(map(int, input().split()))
    Blen = int(input())
    B = set(map(int, input().split()))
    if A - B:
        print(False)
    else:
        print(True)