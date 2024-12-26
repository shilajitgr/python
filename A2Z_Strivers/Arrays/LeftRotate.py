class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not k:
            return
        
        while k > len(nums): # to handle wrapping around multiple times due to k being too large
            k -= len(nums)
        
        nums[:] = nums[-1*k:] + nums[:len(nums)-k]
        
