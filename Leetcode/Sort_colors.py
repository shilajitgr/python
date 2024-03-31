class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_len = len(nums)
        itr = 0
        idx = 0
        """
        Following while loop has O(N^2) time complexity and O(1) space complexity
        """
        while itr < nums_len:
            next = True
            if nums[idx] == 0:
                nums[:] = [0] + nums[:max(idx, 0)] + nums[idx+1:]

            
            if nums[idx] == 2:
                nums[:] = nums[:max(idx, 0)] + nums[idx+1:] + [2]
                next = False
                
            if next:
                idx += 1
            
            itr += 1
        
        """
        # optimal approach
        # Following approach has O(N) time complexity and O(1) space complexity
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
        """
                
sol_obj = Solution()
nums = [2,0,2,1,1,0]
sol_obj.sortColors(nums)
print(nums)
print(nums==[0,0,1,1,2,2])