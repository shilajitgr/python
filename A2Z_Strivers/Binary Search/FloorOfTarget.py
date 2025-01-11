class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self,nums,target):    
        
        # the same code can be used to tell the Insert Position of an a new item into a sorted array
        
        #Your code here
        num_len = len(nums)

        if num_len < 2:
            
            return -1 if nums[0] != target else 0

        low = 0
        high = num_len-1
        mid = (low+high)//2
        lower = num_len 
        # the last index + 1 is the lower bound if the entire array is smaller than target
        while low <= high:

            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] <= target:
                low = mid + 1
                # if target - nums[mid] < min_diff:
                # if mid > lower:   # this and above lines are not needed as, for as long as the search space moves
                # to the right half, the current mid and the value it holds will always be greater than the previous mid
                lower = mid
            
            mid = (low+high)//2
            
        return lower

print(Solution().findFloor([1,2,4,7,7,7,7], 7))