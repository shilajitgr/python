"""
re.findall()
The expression re.findall() returns all the non-overlapping matches of patterns in a string as a list of strings.
Code

# >>> import re
# >>> re.findall(r'\w','http://www.hackerrank.com/')
['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']

re.finditer()
The expression re.finditer() returns an iterator yielding MatchObject instances over all non-overlapping matches for the re pattern in the string.
Code

# >>> import re
# >>> re.finditer(r'\w','http://www.hackerrank.com/')
# <callable-iterator object at 0x0266C790>
# >>> map(lambda x: x.group(),re.finditer(r'\w','http://www.hackerrank.com/'))
['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']
Task
You are given a string . It consists of alphanumeric characters, spaces and symbols(+,-).
Your task is to find all the substrings of  that contains 1 or more vowels.
Also, these substrings must lie in between  consonants and should contain vowels only.

Note :
Vowels are defined as: AEIOU and aeiou.
Consonants are defined as: QWRTYPSDFGHJKLZXCVBNM and qwrtypsdfghjklzxcvbnm.

Input Format

A single line of input containing string s.

Constraints

0 < len(s) < 100

Output Format

Print the matched substrings in their order of occurrence on separate lines.
If no match is found, print -1.

Sample Input

    rabcdeefgyYhFjkIoomnpOeorteeeeet

Sample Output

    ee
    Ioo
    Oeo
    eeeee
"""

import re
vowels = '[AEIOUaeiou]'
cons = '[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]'
p = r'(%s)(%s{2,})(?=%s)' % (cons, vowels, cons)
# this extract the entire matching sequence
# p = r'(%s)(%s{2,})(?=%s)' % (cons, vowels, cons)
# this will extract the entire matching sequence except the last one

m = re.finditer(p, input())
result = list(map(lambda x: x.group(2), m))
# m.group[0] is similar to "".join(list(m.groups()))
# i.e., m.group[0] prints all elements of the group without any space
if result:
    for s in result:
        print(s)
else:
    print(-1)
