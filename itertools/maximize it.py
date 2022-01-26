"""
Sample Input

3 1000  | 3 - no of lists to be provided| 1000 - mod value
2 5 4
3 7 8 9
5 5 7 8 9 10

Sample Output

206

Explanation

Picking 5 from the 1st list, 9 from the 2nd list and 10 from the 3rd list gives the maximum S value equal to
(5^2 + 9^2 + 10^2)%1000 = 206.
"""

from itertools import product

k, M = map(int, input().split())
all_lists = []
for i in range(k):
    all_lists.append(list(map(int, input().split()))[1:])

all_list_product = product(*all_lists)
max_val = 0

for seq in all_list_product:
    sum_val = sum([x ** 2 for x in seq]) % M
    max_val = sum_val if sum_val > max_val else max_val

print(max_val)
