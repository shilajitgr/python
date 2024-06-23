from os import *
from sys import *
from collections import *
from math import *

def getInversions(arr, n) :
	# Write your code here.
    count = 0
    arrLen = n
    for idx in range(0, arrLen):
        first = arr[idx]
        j = idx+1
        for second in arr[j:arrLen]:
            if first > second:
                count += 1
    return count
    
# Taking inpit using fast I/O.
def takeInput() :
    n = int(input())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n

# Main.
arr, n = takeInput()
print(getInversions(arr, n))