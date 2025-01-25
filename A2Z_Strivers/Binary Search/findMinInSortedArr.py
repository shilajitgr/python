class Solution:
    def findMin(self, nums: list[int]) -> int:
        num_len = len(nums)
        print(nums)
        if num_len <= 1:
            return nums[0]

        if num_len == 2:
            
            return nums[0] if nums[0] <= nums[1] else nums[1]

        rotated = False
        if nums[0] >= nums[-1] and nums[0] != nums[1]:
            rotated = True
        
        # find pivot point
        pivot_idx = 0
        if rotated:
            pivot = None
            high = num_len - 1
            low = 0

            while low <= high:

                mid = (low + high) // 2

                if nums[mid] < nums[0]:
                    high = mid - 1
                elif nums[mid] > nums[0]:
                    low = mid + 1
  
                if nums[mid - 1] <= nums[mid] and nums[mid+1] < nums[mid]:
                    # if mid is pointing to the largest element in the array
                    pivot = mid
                    break
                
                if nums[mid - 1] > nums[mid] and nums[mid+1] >= nums[mid]:
                    # if mid is pointing to the smallest element in the array
                    pivot = mid - 1
                    break
       
            pivot_idx = pivot + 1
        
        return nums[pivot_idx]
    
    def findMin2(self, nums: list[int]) -> int:
        num_len = len(nums)
        high = num_len - 1
        low = 0
        
        while low < high:
            mid = (low+high)//2
            
            if nums[mid] > nums[high]:
                low = mid + 1
            elif nums[low] > nums[mid]:
                high = mid
                low += 1
            elif nums[low] < nums[mid] < nums[high]:
                return nums[low]
            else:   # nums[lo] <= nums[mi] <= nums[hi] 
                high -= 1

        return nums[low]
    
arr = [2,2,2,0,1]
arr = [1, 3, 5, 7, 9, 88]
# arr = [1,1,1]
# arr = [3,3,1,3]
print(Solution().findMin2(arr))