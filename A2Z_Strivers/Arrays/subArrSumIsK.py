class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        num_len = len(nums)
        subArr = 0
        for windowSize in range(1,num_len):
            window = sum(nums[:windowSize])
            if window == k:
                subArr += 1
            for idx in range(num_len-windowSize):
                window = window - nums[idx] + nums[windowSize+idx]
                if window == k:
                    subArr += 1
                    
        return subArr
                
print(Solution().subarraySum([1,1,1,4,1,1,1], 2))