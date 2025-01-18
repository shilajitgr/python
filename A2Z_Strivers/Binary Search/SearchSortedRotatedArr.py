class Solution:
    def search(self, nums: list[int], target: int) -> int:
        
        num_len = len(nums)
        print(nums)
        if num_len <= 2:
            if nums[0] == target:
                return 0

            if nums[-1] == target:
                return num_len - 1
            
            return -1

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
        
            nums = nums[pivot_idx:] + nums[:pivot_idx]
            print(nums)
        
        low = 0
        high = num_len - 1
        while low <= high:
            
            mid = (low+high)//2
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                if rotated:
                    if mid < pivot_idx:
                        mid -= (num_len - pivot_idx)
                    else:
                        mid += pivot_idx
                    
                    if mid < 0:
                        mid += num_len
                            
                    if mid >= num_len:
                        mid = mid % num_len
                        
                return mid
            
        return -1 
    
    def searchSortedApt(self, nums: list[int], target: int) -> int:
        
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = (low+high)//2
            
            if nums[mid] == target:
                return mid
            
            if arr[low] <= arr[mid]:    # to check if low to mid is sorted mid to high
                
                if arr[low] <= target < arr[mid]:
                    # if low to mid is sorted, then arr[low] will always be <= arr[mid]
                    # and if targets falls between two values then 
                    # high can be updated to mid - 1
                    high = mid - 1
                else:
                    low = mid + 1
                    
            else:
                
                if arr[mid] < target <= arr[high]:
                    low = mid + 1
                else:
                    high = mid - 1
                    
        return -1

    
# arr, target = [5,6,7,0,1,2,4], 1
# corrected_arr = [0,1,2,4,5,6,7]
# arr, target = [1,2,4,6,7,8,1], 1
arr, target = [3,3,4,5,1,2,3], 2    # invalid test case, all nums to be unique
# arr, target = [4,5,1,2,3], 1
print(arr[Solution().search(arr, target)]==target)
print(arr[Solution().searchSortedApt(arr, target)]==target)
