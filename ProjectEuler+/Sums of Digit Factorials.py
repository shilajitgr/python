"""
Define  as the sum of the factorials of the digits of . For example, .

Define  as the sum of the digits of . So .

Define  to be the smallest positive integer  such that . Though  is ,  is also , and it can be verified that  is .

Define  as the sum of the digits of . So .

Further, it can be verified that  is  and  is .

What is ? As the number can be large, print it modulo .

Input Format

The first line of each test file contains a single integer , which is the number of queries per test file.  lines follow, each containing two integers separated by a single space:  and  of the corresponding query.

Constraints

Output Format

Print exactly  lines, each containing a single integer, which is the answer to the corresponding query.

Sample Input 0

2
3 1000000
20 1000000
Sample Output 0

8
156
Explanation 0

,  and . .

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math


def find_sfn(n):
    fn = sum([math.factorial(int(x)) for x in n])
    sfn = sum([int(x) for x in str(fn)])

    return sfn


def find_gi(sfn):
    small_n = 1
    while True:
        sfn_tmp = find_sfn(str(small_n))
        if sfn == sfn_tmp:
            gi = small_n
            return gi
        small_n += 1


for _ in range(int(input())):
    n = input().split()
    sg = 0
    sfn = find_sfn(n[0])
    # print(f"sf({n[0]}) = {sfn}")
    gi = find_gi(sfn)
    sg = sum([int(x) for x in str(gi)])
    # print(f"g({sfn}) = {gi}")
    # for num in range(1,gi+1):
    #     tmp_gi = find_gi(find_sfn(str(num)))
    #     sg += sum([int(x) for x in str(tmp_gi)])
    print('\n\n')

    print(f"sg({sfn}):{sg % int(n[1])}")
