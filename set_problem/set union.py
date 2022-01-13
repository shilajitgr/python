"""
.union()

The .union() operator returns the union of a set and the set of elements in an iterable.
Sometimes, the | operator is used in place of .union() operator, but it operates only on the set of elements in set.
Set is immutable to the .union() operation (or | operation).

Example

    # >>> s = set("Hacker")
    # >>> print s.union("Rank")
    # set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])
    #
    # >>> print s.union(set(['R', 'a', 'n', 'k']))
    # set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])
    #
    # >>> print s.union(['R', 'a', 'n', 'k'])
    # set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])
    #
    # >>> print s.union(enumerate(['R', 'a', 'n', 'k']))
    # set(['a', 'c', 'r', 'e', (1, 'a'), (2, 'n'), 'H', 'k', (3, 'k'), (0, 'R')])
    #
    # >>> print s.union({"Rank":1})
    # set(['a', 'c', 'r', 'e', 'H', 'k', 'Rank'])
    #
    # >>> s | set("Rank")
    # set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])


---------------------------------------------------
.intersection()
The .intersection() operator returns the intersection of a set and the set of elements in an iterable.
Sometimes, the & operator is used in place of the .intersection() operator, but it only operates on the set of elements in set.
The set is immutable to the .intersection() operation (or & operation).

Example:
    # >>> s = set("Hacker")
    # >>> print s.intersection("Rank")
    # set(['a', 'k'])
    #
    # >>> print s.intersection(set(['R', 'a', 'n', 'k']))
    # set(['a', 'k'])
    #
    # >>> print s.intersection(['R', 'a', 'n', 'k'])
    # set(['a', 'k'])
    #
    # >>> print s.intersection(enumerate(['R', 'a', 'n', 'k']))
    # set([])
    #
    # >>> print s.intersection({"Rank":1})
    # set([])
    #
    # >>> s & set("Rank")
    # set(['a', 'k'])

---------------------------------------------------
.difference()
The tool .difference() returns a set with all the elements from the set that are not in an iterable.
Sometimes the - operator is used in place of the .difference() tool, but it only operates on the set of elements in set.
Set is immutable to the .difference() operation (or the - operation).

    # >>> s = set("Hacker")
    # >>> print s.difference("Rank")
    # set(['c', 'r', 'e', 'H'])
    #
    # >>> print s.difference(set(['R', 'a', 'n', 'k']))
    # set(['c', 'r', 'e', 'H'])
    #
    # >>> print s.difference(['R', 'a', 'n', 'k'])
    # set(['c', 'r', 'e', 'H'])
    #
    # >>> print s.difference(enumerate(['R', 'a', 'n', 'k']))
    # set(['a', 'c', 'r', 'e', 'H', 'k'])
    #
    # >>> print s.difference({"Rank":1})
    # set(['a', 'c', 'e', 'H', 'k', 'r'])
    #
    # >>> s - set("Rank")
    # set(['H', 'c', 'r', 'e'])

---------------------------------------------------
.symmetric_difference()
The .symmetric_difference() operator returns a set with all the elements that are in the set and the iterable but not both.
Sometimes, a ^ operator is used in place of the .symmetric_difference() tool, but it only operates on the set of elements in set.
The set is immutable to the .symmetric_difference() operation (or ^ operation).

    # >>> s = set("Hacker")
    # >>> print s.symmetric_difference("Rank")
    # set(['c', 'e', 'H', 'n', 'R', 'r'])
    #
    # >>> print s.symmetric_difference(set(['R', 'a', 'n', 'k']))
    # set(['c', 'e', 'H', 'n', 'R', 'r'])
    #
    # >>> print s.symmetric_difference(['R', 'a', 'n', 'k'])
    # set(['c', 'e', 'H', 'n', 'R', 'r'])
    #
    # >>> print s.symmetric_difference(enumerate(['R', 'a', 'n', 'k']))
    # set(['a', 'c', 'e', 'H', (0, 'R'), 'r', (2, 'n'), 'k', (1, 'a'), (3, 'k')])
    #
    # >>> print s.symmetric_difference({"Rank":1})
    # set(['a', 'c', 'e', 'H', 'k', 'Rank', 'r'])
    #
    # >>> s ^ set("Rank")
    # set(['c', 'e', 'H', 'n', 'R', 'r'])

Input Format

The first line contains an integer, , the number of students who have subscribed to the English newspaper.
The second line contains  space separated roll numbers of those students.
The third line contains , the number of students who have subscribed to the French newspaper.
The fourth line contains  space separated roll numbers of those students.

Constraints


Output Format

Output the total number of students who have at least one subscription.

Sample Input

9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8


Sample Output

13
"""

english_count = int(input())
english_roll = set(map(int, input().split()))
french = int(input())
french_roll = set(map(int, input().split()))

print(len(english_roll ^ french_roll))