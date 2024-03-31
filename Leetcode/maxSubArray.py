"""
Kadane's Algorithm

In computer vision, maximum-subarray algorithms are used on bitmap images to 
detect the brightest area in an image.

In computer science, the maximum sum subarray problem, also known as the 
maximum segment sum problem, is the task of finding a contiguous subarray 
with the largest sum, within a given one-dimensional array A[1...n] of numbers. 
It can be solved in O(n) and O(1) space.
"""

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        nums_len = len(nums)

        if nums_len == 1:
            return nums[0]

        max_val = max(max(nums), sum(nums))

        # brute force
        # for window_size in range(nums_len, 0, -1):
        #     for idx in range(nums_len - window_size + 1):
        #         tmp_sum = sum(nums[idx: idx+window_size])
        #         if tmp_sum > max:
        #             max = tmp_sum

        tmp_sum = 0
        for i in nums:
            tmp_sum += i
            if tmp_sum < 0:
                tmp_sum = 0
                continue
                
            if tmp_sum > max_val:
                max_val = tmp_sum

        return max_val
    

sol_obj = Solution()
nums = [-1,-2,-2,-2,3,2,-2,0]
print(sol_obj.maxSubArray(nums)==5)