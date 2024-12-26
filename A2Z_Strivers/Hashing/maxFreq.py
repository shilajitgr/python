class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        min_val = min(nums)
        max_val = max(nums)
        
        freq = [0] * (max_val - min_val + 1)
        for i in nums:
            freq[i - min_val] += 1
            
        print(freq)
        
        
        
        return max(freq)
            
            
obj = Solution()
print(obj.maxFrequency([1,4,8,13], 5))

"""
data = [1,1,4,4,5,6,11,12,13]
diff = [0,0,3,0,1,1,5,1,1]
"""