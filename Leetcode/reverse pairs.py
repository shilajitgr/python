class Solution:

    def merge(self, left: list[int], right: list[int]) -> list[int]:
        combined_arr = []
        left_len = len(left)
        right_len = len(right)
        l_idx = 0
        r_idx = 0
        while len(combined_arr) != (left_len + right_len):

            if l_idx == left_len:
                combined_arr += right[r_idx:]
                return combined_arr
            if r_idx == right_len:
                combined_arr += left[l_idx:]
                return combined_arr
            
            if left[l_idx] < right[r_idx]:
                combined_arr.append(left[l_idx])
                l_idx+=1
            else:
                combined_arr.append(right[r_idx])
                r_idx+=1


    def count_pair(self, left: list[int], right: list[int]) -> int:
        count = 0
        j = 0
        for left_num in left:
            while j < len(right):

                if (right[j]+right[j]) >= left_num:
                    break

                j+=1

            count += j
        return count

    def merge_count(self, nums: list[int]) -> tuple[int, list[int]]:
        count = 0
        
        if len(nums) < 2:
            return nums, count

        mid = len(nums)//2
        
        left_arr, left_count = self.merge_count(nums[:mid])
        right_arr, right_count = self.merge_count(nums[mid:])
        count = self.count_pair(left_arr, right_arr) + left_count + right_count
        result = self.merge(left_arr, right_arr) 
        return result, count

    def reversePairs(self, nums: list[int]) -> int:
        
        _, count = self.merge_count(nums)

        return count
    

obj = Solution()

print(obj.reversePairs([1,3,2,3,1]))