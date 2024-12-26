class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        low = mid = 0
        high = len(nums) - 1
        if high == 0:
            return

        while mid <= high:
            
            if nums[mid] == 0:
                nums[mid], nums[low] = nums[low], nums[mid]
                low += 1
                mid += 1
                continue
            
            if nums[mid] == 2:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
                continue

            if nums[mid] == 1:
                mid += 1
                continue
            
nums = [2,2,2,0,2,1,1,0,0,0,1,2,1]

Solution().sortColors(nums)

print(nums)