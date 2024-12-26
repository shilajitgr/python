class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last = len(nums) - 1
        breakpoint = -1

        # Find the first decreasing element from the end
        for i in range(last, 0, -1):
            if nums[i] > nums[i - 1]:
                breakpoint = i - 1
                break

        if breakpoint == -1:  # If no breakpoint is found, reverse the entire list
            nums.reverse()
            return

        # Find the idx of smallest element larger than nums[breakpoint] to the right of it
        i = last
        while nums[i] <= nums[breakpoint]:
                i -= 1

        nums[breakpoint], nums[i] = nums[i], nums[breakpoint]

        # Reverse the elements to the right of the breakpoint
        nums[breakpoint + 1:] = reversed(nums[breakpoint + 1:])
        
sol_obj = Solution()
nums = [1,3,2]
sol_obj.nextPermutation(nums)
print(nums==[2,1,3])