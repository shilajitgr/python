class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        # a list of sorted pair of duplicate elements will occupy indices
        # in the order (even, odd) but after encountering the non-dup element
        # the order will be altered to (odd, even)
        #  0 1  2  3 4  5 6  7 8
        # (e o)(e)(o e)(o e)(o e)
        #  1 1  2  3 3  4 4  8 8
        num_len = len(nums)
        high = num_len - 1
        low = 0
        if high == 0:
            return nums[0]
        
        while low <= high:
            
            mid = (low+high)//2
            
            if mid == 0 or mid == num_len - 1:
                return nums[mid]
            
            if mid%2 == 0:
                if nums[mid] == nums[mid+1]:
                    low = mid + 1
                elif nums[mid] == nums[mid-1]:
                    high = mid - 1
                else:
                    return nums[mid]
            else:
                if nums[mid] == nums[mid-1]:
                    low = mid+1
                elif nums[mid] == nums[mid+1]:
                    high = mid - 1
                else:
                    return nums[mid]
                
    
arr = [1,1,2,3,3,4,4,8,8]
arr = [3,3,7,7,10,11,11]
arr = [1,1,2]

print(Solution().singleNonDuplicate(arr))