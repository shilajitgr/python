class Solution:
    def rearrangeEvenLenArray(self, nums: list[int]) -> list[int]:
        """
        the number of negative and positive integers always match
        """

        num_len = len(nums)
        queue = [0]*num_len
        j = 0
        k = 1
        for i in range(num_len):
            if nums[i] < 0:
                queue[k] = nums[i]
                k+=2
            else:
                queue[j] = nums[i]
                j+=2

        return queue
    
    def rearrangeUnEvenLenArray(self, nums: list[int]) -> list[int]:
        """
        the number of negative and positive integers do not match
        """

        num_len = len(nums)
        queue = [0]*num_len
        j = 0
        k = 1
        
        neg_count = len([num for num in nums if num < 0])
        remaining = 1 if neg_count < num_len//2 else -1
            
        for i in range(num_len):
            if nums[i] < 0:
                queue[k] = nums[i]
                k+=2
            else:
                queue[j] = nums[i]
                j+=2

        return queue