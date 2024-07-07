# Extended Boyer Moore’s Voting Algorithm : Logic behind it, is that,
# if >n/3 is majority mark then only 2 majority elements are possible in total

class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        majority_mark = len(nums)//3
        hash = {}
        final = set()

        for num in nums:
            hash[f"{num}"] = hash.get(f"{num}",0) + 1 
            if hash[f"{num}"] > majority_mark:
                final.add(num)

        return list(final)