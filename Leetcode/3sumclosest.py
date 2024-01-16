class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        num_len = len(nums)
        if num_len == 3:
            return sum(nums)

        closest = nums[-3] + nums[-2] + nums[-1]
        
        for x in range(num_len-2):
            i = x + 1
            j = num_len - 1

            while i < j:
                sum_data = nums[x] + nums[i] + nums[j]
                
                if sum_data > target:
                    j -= 1
                elif sum_data < target:
                    i += 1
                else:
                    return target

                if abs(target - closest) > abs(target - sum_data):
                    closest = sum_data
                
        return closest
    
print(Solution().threeSumClosest([-1,2,1,-4], 1))