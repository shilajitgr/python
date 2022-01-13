"""
problem statement:
https://www.hackerrank.com/challenges/symmetric-difference/problem?isFullScreen=true
"""

msize, m = input(), set(map(int, input().split()))
nsize, n = input(), set(map(int, input().split()))

sym_diff = sorted(m.symmetric_difference(n))
print(*sym_diff, sep="\n")
