from functools import reduce
class Solution:

    def maxProduct(self, nums: list[int]) -> int:

        num_len = len(nums)
        maxNum = max(nums)
        maxProd = reduce(lambda x,y:x*y, nums)
        prefix = 1
        suffix = 1
        for idx in range(num_len):

            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1

            prefix *= nums[idx]
            suffix *= nums[num_len-idx-1]
            maxProd = max(prefix, suffix, maxProd)
        
        return max(maxNum,maxProd)
    
arr = [0,0,2,3,12,0,-2,45,0,-2,3,8,-9,0,0]
arr = [0,0,0,1,-45,0,9,3,-3,0,7,0,21]
arr = [-1,-2,-3,0]
print(Solution().maxProduct(arr))