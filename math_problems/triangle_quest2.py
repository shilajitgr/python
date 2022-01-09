"""
You are given a positive integer N.
Your task is to print a palindromic triangle of height N.

For example, a palindromic triangle of size 5 is:

1
121
12321
1234321
123454321
"""

for i in range(1, int(input()) + 1):  # More than 2 lines will result in 0 score. Do not leave a blank line also
    # print(*(range(1, i + 1)), *(range(i - 1, 0, -1)), sep='')  #this works too
    print([1, 11, 111, 1111, 11111, 111111, 1111111, 11111111, 111111111, 1111111111][i - 1] *
          [1, 11, 111, 1111, 11111, 111111, 1111111, 11111111, 111111111, 1111111111][i - 1])
