class Solution:
    # optimal
    # using prefix sum
    def subarraySum(self, nums: list[int], k: int) -> int:
        num_len = len(nums)
        subArr = 0
            
        remember = {}
        remember[0] = 1
        prefix = 0
        for idx in range(num_len):
            prefix += nums[idx]
            if prefix - k in remember:
                subArr += remember[prefix - k]
            remember[prefix] = remember.setdefault(prefix,0) + 1
                    
        return subArr
                
print(Solution().subarraySum([1,1,1,4,1,1,1], 2))