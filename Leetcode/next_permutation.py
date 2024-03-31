class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        breakpoint = None
        last = len(nums) - 1
        for i in range(last, 0, -1):
            if nums[i] > nums[i-1]:
                breakpoint = i - 1
                break

        if breakpoint == None:
            nums.reverse()
            return

        if len(nums[breakpoint+1:]) == 1:
        
            nums[breakpoint], nums[last] = nums[last], nums[breakpoint]
            return

        #find value closest to nums[breakpoint] to the right of the list
        min = max(nums)
        idx = None
        for x in range(len(nums[breakpoint+1:])):
            if nums[breakpoint+1+x] > nums[breakpoint] and nums[breakpoint+1+x] - nums[breakpoint] <= min:
                min = nums[breakpoint+1+x] - nums[breakpoint]
                idx = breakpoint+1+x
                
        nums[breakpoint], nums[idx] = nums[idx], nums[breakpoint]
                
        sublist = nums[breakpoint+1:]
        sublist.reverse()

        nums[breakpoint+1:] = sublist
        
        
sol_obj = Solution()
nums = [2,3,1,3,3]
sol_obj.nextPermutation(nums)
print(nums==[2,3,3,1,3])