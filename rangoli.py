"""
You are given an integer, N. Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art
based on creation of patterns.)

Different sizes of alphabet rangoli are shown below:

#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
"""


def print_rangoli(size):
    # your code goes here

    reqAscii = ord('a') + size - 1
    num = size
    quarterlist = []
    for i in range(0, size):
        j = 0
        word = []
        while j <= i:
            word.append(str(chr(reqAscii - j)))
            j += 1
        # word = prefix + "-".join(word)
        word = "-".join(word).rjust((size-1)*2+1, "-")
        quarterlist.append(word)
    for word in quarterlist:
        word += word[::-1][1:]
        print(word)
    for word in quarterlist[::-1][1:]:
        word += word[::-1][1:]
        print(word)


if __name__ == '__main__':
    n = 3
    print_rangoli(n)
