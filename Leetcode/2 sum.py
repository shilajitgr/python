class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Brute-Force
        # for idx in range(len(nums)-1):
        #     new_target = target - nums[idx]
        #     for idx2 in range(len(nums[idx+1:])):
        #         if nums[idx+idx2+1] == new_target:
        #             return [idx,idx+idx2+1]

        # using dict
        element_map = {}

        for idx in range(len(nums)):
            new_target = target - nums[idx]
            if new_target in element_map:
                return [element_map[new_target], idx]
            else:
                element_map[nums[idx]] = idx
        
        # Two-pointer approach needs the array to be sorted first
    
obj = Solution()
print(obj.twoSum([-1,-2,-3,-4,-5],-8))