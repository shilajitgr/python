class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        num_len = len(nums)
        if num_len == 3:
            return [] if sum(nums) != 0 else [nums]

        zero_list = []
        item_hash = {}
        
        for x in range(num_len-2):
            i = x + 1
            j = num_len - 1
            target = -1 * nums[x]

            while i < j:
                sum_data = nums[i] + nums[j]
                if sum_data > target:
                    j -= 1
                elif sum_data < target:
                    i += 1
                else:
                    temp = [nums[x], nums[i], nums[j]]
                    i += 1
                    j -= 1
                    if f"{temp}" not in item_hash:
                        zero_list.append(temp)
                        item_hash[f"{temp}"] = ""
                
        return zero_list

simple = [3,0,-2,-1,1,2]
print(Solution().threeSum(simple))
