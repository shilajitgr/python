"""
A set is an unordered collection of elements without duplicate entries.
When printed, iterated or converted into a sequence, its elements will appear in an arbitrary order.

Example:
    >>> print set()
    set([])

    >>> print set('HackerRank')
    set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])

    >>> print set([1,2,1,2,3,4,5,6,0,9,12,22,3])
    set([0, 1, 2, 3, 4, 5, 6, 9, 12, 22])

    >>> print set((1,2,3,4,5,5))
    set([1, 2, 3, 4, 5])

    >>> print set(set(['H','a','c','k','e','r','r','a','n','k']))
    set(['a', 'c', 'r', 'e', 'H', 'k', 'n'])

    >>> print set({'Hacker' : 'DOSHI', 'Rank' : 616 })
    set(['Hacker', 'Rank'])

    >>> print set(enumerate(['H','a','c','k','e','r','r','a','n','k']))
    set([(6, 'r'), (7, 'a'), (3, 'k'), (4, 'e'), (5, 'r'), (9, 'k'), (2, 'c'), (0, 'H'), (1, 'a'), (8, 'n')])

Function Description

Complete the average function in the editor below.

average has the following parameters:

int arr: an array of integers
Returns

float: the resulting float value rounded to 3 places after the decimal
Input Format

The first line contains the integer, N, the size of arr[].
The second line contains the N space-separated integers, arr[i].

"""

def average(array):
    # your code goes here
    num = sum(set(array))
    return num/float(len(set(array)))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)