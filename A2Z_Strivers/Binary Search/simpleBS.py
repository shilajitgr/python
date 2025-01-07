class Solution:
    def search(self, nums: list[int], target: int) -> int:
        num_len = len(nums)

        if num_len < 2:
            
            return -1 if nums[0] != target else 0

        low = 0
        high = num_len-1
        mid = (low+high)//2
        
        while low <= high:

            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                return mid
            
            mid = (low+high)//2
            
        return -1
    
arr = [-1,0,3,5,9,12]
print(Solution().search(arr, 2))