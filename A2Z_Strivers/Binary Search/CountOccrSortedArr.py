class Solution:
    def countFreq(self, nums, target):
        
        last = -1
        first = -1
        
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            
            mid = (low+high) // 2
            
            if nums[mid] >= target:
                high = mid - 1
                first = mid
            else:
                low = mid + 1
                
        
        if nums[first] != target:
            return 0
        
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            
            mid = (low+high) // 2
            
            if nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
                last = mid
        
        
        return last - first + 1
    
    
arr = [1, 1, 2, 2, 2, 2, 3]
print(Solution().countFreq(arr, 2))