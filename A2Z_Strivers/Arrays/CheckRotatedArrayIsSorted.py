class Solution:
    def check(self, nums: list[int]) -> bool:
        count = 0
        arr_len = len(nums)
        pivot = False
        for idx in range(arr_len-1):
            if nums[idx] <= nums[idx+1]:
                count += 1
            else:
                if not pivot:
                    pivot = True
                    continue
                return False
        
        if pivot and nums[-1] <= nums[0]:
            count += 1
            
        if count == arr_len-1:
            return True
        
        return False
    
print(Solution().check([1,1,1]))