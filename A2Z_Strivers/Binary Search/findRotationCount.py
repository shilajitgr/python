class Solution:
    
    def find_pivotIdx(self, arr):
        return self.findKRotation(arr)
    
    def findKRotation(self, arr):
        # code here
        arr_len = len(arr)
        nums = arr
        high = arr_len - 1
        low = 0
        
        while low < high:
            mid = (low+high)//2
            
            if nums[mid] > nums[high]:
                low = mid + 1
            elif nums[low] > nums[mid]:
                high = mid
                low += 1
            elif nums[low] < nums[mid] < nums[high]:
                break
            else:
                high -= 1
        
        return low