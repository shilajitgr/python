"""
Consider the following:

A string, s, of length n where s=c0c1c2c3c4...cN.
An integer, k, where k is a factor of n.
We can split s into n/k substrings where each subtring, ti, consists of a contiguous block of k characters in s.
Then, use each ti to create string ui such that:

The characters in ui are a subsequence of the characters in ti.
Any repeat occurrence of a character is removed from the string such that each character in ui occurs exactly once.
In other words, if the character at some index j in ti occurs at a previous index<j  in ti, then do not include
the character in string ui.
Given s and k, print n/k lines where each line i denotes string ui.

Example:

    s = "AAABCADDE"
    k = 3

There are three substrings of length  to consider: 'AAA', 'BCA' and 'DDE'. The first substring is all 'A' characters, so u1="A".
The second substring has all distinct characters,so u2="BCA". The third substring has 2 different characters,so u3="DE".
Note that a subsequence maintains the original order of characters encountered.
The order of characters in each subsequence shown is important.
"""


def merge_the_tools(string, k):
    # your code goes here
    i = 0
    while i < len(string) // k:
        sub_seq = string[i * k:(i + 1) * k]
        i += 1
        l = []
        for j in sub_seq:
            if j not in l:
                l.append(j)
        print("".join(l))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
