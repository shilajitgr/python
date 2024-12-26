class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        
        size = len(nums)
        
        return size*(size+1)//2 - sum(nums)
    
        """XOR Solution
        XOR Truth Table:

        n ^ n = 0
        n ^ 0 = n
        n ^ m = m ^ n
        
        So, now if we XOR all the elements in the array with all the numbers from 0 to n, we will be left with the missing number.
        
        def missingNumber(self, nums: List[int]) -> int:
            n = len(nums)
            ans = 0
            for i in range(1, n + 1):
                ans ^= i
            for num in nums:
                ans ^= num
            return ans
        """