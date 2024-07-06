class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        majority_mark = len(nums)//2
        hash = {}

        for num in nums:
            hash[f"{num}"] = hash.get(f"{num}",0) + 1 
            if hash[f"{num}"] > majority_mark:
                return num
            
        """
        Moore's voting Algorithm
        count = 0
        element = None

        for num in nums:
            if count == 0:
                element = num
                count = 1
            else:
                count = count + 1 if num == element else count - 1

        return element"""
    
    
obj = Solution()

print(obj.majorityElement([6,5,5]))