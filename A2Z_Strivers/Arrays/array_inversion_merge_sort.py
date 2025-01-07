
arr = [6,2,3,5,1,8,7,3]
# arr = [2, 4, 1, 3, 5]

def merge(arr_left: list[int], arr_right: list[int], inversions: int) -> tuple[list[int], int]:
    len_right = len(arr_right)
    len_left = len(arr_left)
    combined_arr = []
    combined_len = len(arr_left+arr_right)
    i = 0
    j = 0
    while len(combined_arr) != combined_len:
        
        if j == len_right:
            combined_arr.extend(arr_left[i:])
            break
        if i == len_left:
            combined_arr.extend(arr_right[j:])
            break
        
        if arr_left[i] > arr_right[j]:
            print(arr_left[i], arr_right[j],sep="||")
            val = arr_right[j]
            j += 1
            inversions += len(arr_left[i:])
        else:
            val = arr_left[i]
            i += 1

        combined_arr.append(val)
        
    return (combined_arr, inversions)


def merge_sort(array: list[int], inversions: int):

    if len(array) < 2:
        return array, inversions
    else:
        mid = len(array)//2
        arr_left, inversions = merge_sort(array[:mid], inversions)
        arr_right, inversions = merge_sort(array[mid:], inversions)
        
        result, inversions = merge(arr_left, arr_right, inversions)
        print(result)
        return result, inversions
    
"""
## without using extra space (optimal solution)

import math

class Solution:
    #User function Template for python3
    #Function to count inversions in the array.
    
    def inversionCount(self, arr):
        # Your Code Here
        n = len(arr)
        count = self.mergeSort(arr, 0, n - 1)
        return count
        
    def merge(self, arr, low, mid, high):
        temp = []   # temporary array
        left = low  # starting index of left half of arr
        right = mid + 1 # starting index of right half of arr
    
        cnt = 0     # Modification 1: cnt variable to count the pairs
    
        # storing elements in the temporary array in a sorted manner
        while (left <= mid and right <= high):
            if (arr[left] <= arr[right]):
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                cnt += (mid - left + 1)  # Modification 2
                right += 1
    
        # if elements on the left half are still left
        while (left <= mid):
            temp.append(arr[left])
            left += 1
    
        # if elements on the right half are still left
        while (right <= high):
            temp.append(arr[right])
            right += 1
    
        # transfering all elements from temporary to arr
        for i in range(low, high + 1):
            arr[i] = temp[i - low]
    
        return cnt   # Modification 3

    def mergeSort(self, arr, low, high):
        cnt = 0
        if low >= high:
            return cnt
        mid = math.floor((low + high) / 2)
        cnt += self.mergeSort(arr, low, mid)    # left half
        cnt += self.mergeSort(arr, mid + 1, high)  # right half
        cnt += self.merge(arr, low, mid, high)  # merging sorted halves
        return cnt
"""

print("-"*80)
print(*merge_sort(arr,0), sep=", ")