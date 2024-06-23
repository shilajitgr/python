class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        breakpoint = None
        last = len(nums) - 1
        for i in range(last, 0, -1):
            # 1 241 42 52 6 3 2 0
            if nums[i] > nums[i-1]:
                breakpoint = i - 1
                break
            # 52 is breakpoint 

        if breakpoint == None: # this will happen only if the array is sorted in descending order
            nums.reverse()
            return

        if len(nums[breakpoint+1:]) == 1: # if only one element is present to the right of breakpoint
        
            nums[breakpoint], nums[last] = nums[last], nums[breakpoint]
            return

        #find lower value closest to nums[breakpoint] to its right in the list
        min = max(nums)
        idx = None
        for x in range(len(nums[breakpoint+1:])):
            if 0 < nums[breakpoint+1+x] - nums[breakpoint] <= min:
                min = nums[breakpoint+1+x] - nums[breakpoint]
                idx = breakpoint+1+x
        # here nums[idx] points to 6
        nums[breakpoint], nums[idx] = nums[idx], nums[breakpoint]
        # nums = 1 241 42 6 52 3 2 0
        sublist = nums[breakpoint+1:]
        sublist.reverse()
        # sublist = 0 2 3 52
        nums[breakpoint+1:] = sublist
        # nums = 1 241 42 6 0 3 2 52
        
sol_obj = Solution()
nums = [1,3,2]
sol_obj.nextPermutation(nums)
print(nums==[2,1,3])