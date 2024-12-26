class Solution:
    
    """
    # Optimized Solution
    
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j
    """

    def removeDuplicates(self, nums: list[int]) -> int:

        arr_len = len(nums)
        unique_len = arr_len
        idx = 0
        max_val = max(nums)
        while idx < (arr_len-1):
            one_dup = 0
            start = idx
            
            while idx+one_dup+1 < arr_len and nums[start] == nums[idx+one_dup+1]:
                one_dup += 1
            
            if one_dup:
                nums[start+1:] = nums[start+one_dup+1:] + nums[start+1:start+one_dup+1]
                unique_len -= one_dup
                
            if nums[start] == max_val:
                break
            
            idx += 1
            
        return unique_len


print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4,4])) # 5
        