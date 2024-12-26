class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        total = 0
        unique = []
        for i in range(len(nums)):
            if nums[i] != 0:
                unique.append(nums[i])
                total += 1
        
        nums[:] = unique[:] + [0] * (len(nums)-total)
        
        """
        # Optimized Solution: Reducing space complexity
        
        last_idx = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_idx] = nums[i]
                last_idx += 1

        
        nums[last_idx:] = [0] * (len(nums)-last_idx)
        """ 

nums = [0,1,0,3,12]
Solution().moveZeroes(nums)
print(nums)
