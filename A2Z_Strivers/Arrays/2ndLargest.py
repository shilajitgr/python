class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        max_num = arr[0]
        sec_num = -1
        for num in arr:
            if num > max_num:
                sec_num, max_num = max_num, num
            elif sec_num < num < max_num:
                sec_num = num
        
        if sec_num == max_num:
            return -1
            
        return sec_num
    
print(Solution().getSecondLargest([17296,9524,28446,12750,422,7888,25584]))