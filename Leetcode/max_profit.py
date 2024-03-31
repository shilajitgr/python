class Solution:
    def maxProfit(self, nums: list[int]) -> int:
        """
        Observation:

        1) start price has to be the lowest value
        """

        num_len = len(nums)
        profit = 0
        if num_len < 2:
            return profit

        # check if its sorted in ascending order
        reverse_sorted = True
        for i in range(num_len-1):
            if nums[i] < nums[i+1]:
                reverse_sorted = False
                break
        
        if reverse_sorted:
            return profit

        if num_len == 2:
            return nums[1] - nums[0]

        # return self.brute_force(nums)
        min_val_idx = 0
        max_val_idx = 0
        
        for i in range(num_len):
            
            if nums[i] < nums[min_val_idx]:
                min_val_idx = i
                max_val_idx = i
                continue 

            if nums[i] >= nums[max_val_idx]:
                max_val_idx = i

            if nums[max_val_idx] - nums[min_val_idx] > profit:
                    profit = nums[max_val_idx] - nums[min_val_idx]
        
        return profit
    
    def brute_force(self, nums:list) -> int:
        num_len = len(nums)
        start = 0
        end = 1
        profit = max(nums[end] - nums[start], profit)
        while start < num_len:
            
            if nums[start] > nums[start+1]:
                start += 1
            
            end += 1
            
            if end == num_len:
                start += 1
                end = start + 1
                if end >= num_len:
                    break
                
            if nums[end] - nums[start] > profit:
                profit = nums[end] - nums[start]
                
        return profit
    
    
sol_obj = Solution()
nums = [7,1,5,3,6,4] # [0,-6,4,-2,3,-2]
print(sol_obj.maxProfit(nums)==5)
nums = [7,6,4,3,1]
print(sol_obj.maxProfit(nums)==0)
nums = [1,2,4]
print(sol_obj.maxProfit(nums)==3)