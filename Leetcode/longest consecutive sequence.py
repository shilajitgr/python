class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        set_nums = set(nums)
        longest = 0
        
        for num in nums:
            cnt = 0
            if num-1 not in set_nums:
                while num in set_nums:
                    cnt+=1
                    num+=1
            if cnt > longest:
                longest = cnt
        
        return longest
    
"""
Optimal Solution

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = set(nums)
        table = {}
        maxval = 0
        for num in nums:
            x = table.get(num - 1, 0)
            y = table.get(num + 1, 0)
            val = x + y + 1
            table[num - x] = val
            table[num + y] = val
            maxval = max(maxval, val)

            # print(f"num = {num}, x = {x}, y = {y}, val = {val}, table = {table}")
        return maxval
"""
            

obj = Solution()
print(obj.longestConsecutive([100,4,200,1,3,2, 10001, 10002, 10003, 10004, 10005]))
# print(obj.longestConsecutive([0,0]))