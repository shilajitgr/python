class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        num_len = len(nums)
        final = set()
        index_tracker = set()
        
        for idx in range(num_len):
            new_target = 0 - nums[idx]

            seen = {}
            # seen.add(nums[idx])
            for new_idx in range(idx+1, num_len):
                temp = tuple(sorted([idx, seen.get(new_target - nums[new_idx],0), new_idx]))
                if new_target - nums[new_idx] in seen and temp not in index_tracker :
                    final.add(tuple(sorted([nums[temp[0]], nums[temp[1]] ,nums[temp[2]]])))
                    index_tracker.add(temp)

                seen[nums[new_idx]] = new_idx

        return [list(x) for x in final]
    
simple = [3,0,-2,-1,1,2]
simple = [-1,0,1,2,-1,-4]
print(Solution().threeSum(simple))
