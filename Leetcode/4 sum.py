class Solution:
    def twoSum(self,nums: list[int], target: int) -> list[list[int]]:
        element_map = {}
        sol = set()
        
        for idx in range(len(nums)):
            new_target = target - nums[idx]
            if new_target in element_map and tuple([nums[idx], new_target]) not in sol:
                sol.add(tuple([new_target,nums[idx]]))
            else:
                element_map[nums[idx]] = idx
        return [[]] if not sol else list(sol)

    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums_len = len(nums)
        nums.sort()
        sol = set()
        if nums_len == 4 and sum(nums) == target:
                return [nums]
        for idx1 in range(nums_len-3):
            if idx1 != 0 and nums[idx1] == nums[idx1-1]: # skipping over adjancent duplicates
                    continue
            for idx2 in range(idx1+1, nums_len-2):
                if nums[idx2] == nums[idx2-1] and idx2 != idx1+1:
                    continue
                new_target = target - (nums[idx1]+nums[idx2])
                offset = idx2+1
                vals = self.twoSum(nums[offset:], new_target)
                for val in vals:
                    if not val:
                        continue
                    sol.add(tuple([nums[idx1], nums[idx2], val[0], val[1]]))
        return list(sol)


obj = Solution()
set1 = [1,0,-1,0,-2,2]
set2 = [-2,-1,-1,1,1,2,2]
set3 = [-3,-2,-1,0,0,1,2,3]
set4 = [-5,5,4,-3,0,0,4,-2]
print(obj.fourSum(set4, 0))
