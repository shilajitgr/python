class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        
        last = -1
        first = -1
        num_len = len(nums)
        
        if num_len == 0:
            return [-1, -1]
        
        low = 0
        high = num_len - 1
        
        while low <= high:
            
            mid = (low+high) // 2
            
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] >= target:
                high = mid - 1
                if nums[mid] == target:
                    first = mid
                
        
        low = 0
        high = num_len - 1
        
        while low <= high:
            
            mid = (low+high) // 2
            
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] <= target:
                low = mid + 1
                if nums[mid] == target:
                    last = mid
        
        return [first, last]
            
        

arr = [1, 1, 2, 2, 2, 2, 3]
print(Solution().searchRange(arr, 2))