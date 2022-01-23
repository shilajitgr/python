"""
https://www.hackerrank.com/challenges/iterables-and-iterators/problem

Input Format

The input consists of three lines. The first line contains the integer N, denoting the length of the list. The next line
consists of N space-separated lowercase English letters, denoting the elements of the list.

The third and the last line of input contains the integer k, denoting the number of indices to be selected.

Output Format

Output a single line consisting of the probability that at least one of the k indices selected contains the letter:'a'.
"""

from itertools import combinations

list_len = int(input())
char_list = input().split()
k = int(input())

combo = list(combinations(char_list, k))
total_seq = len(combo)

reqd_seq = [1 for x in combo if 'a' in x]

print(len(reqd_seq)/total_seq)