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
        sub_arrays = []
        tmp_sum = 0
        cur_start = 0
        for i in range(nums_len):
            tmp_sum += nums[i]
            if tmp_sum < 0:
                tmp_sum = 0
                cur_start = i + 1
                continue
                
            if tmp_sum > max_val:
                max_val = tmp_sum
                sub_arrays = [nums[cur_start:i+1]]
            elif tmp_sum == max_val:
                sub_arrays.append(nums[cur_start:i+1])
                
        print(sub_arrays)
        return max_val
    
    def maxSubArray2D(self, matrix: list[list[int]]) -> int:
        """
        Given a 2D array, find the maximum sum subarray in it.
        """
        
        rows = len(matrix)
        cols = len(matrix[0])
        max_sum = float('-inf')

        for left in range(cols):
            temp = [0] * rows
            for right in range(left, cols):
                for i in range(rows):
                    temp[i] += matrix[i][right]
                current_max_sum = self.kadane(temp)
                max_sum = max(max_sum, current_max_sum)

        return max_sum
        
    def kadane(self, arr):
        max_sum = float('-inf')
        current_sum = 0
        for num in arr:
            current_sum = current_sum + num
            max_sum = max(max_sum, current_sum)
        return max_sum
    

# Example usage
matrix = [
    [ 1,  2, -1, -4, -20],
    [-8, -3,  4,  2,   1],
    [ 3,  8, 10,  1,   3],
    [-4, -1, 18,  7,  -6]
]

# print(Solution().maxSubArray2D(matrix))  # Output: 29


sol_obj = Solution()
nums = [4,1,-1,-2,-2,-2,3,2,-2,0,]
print(sol_obj.maxSubArray(nums)==5)