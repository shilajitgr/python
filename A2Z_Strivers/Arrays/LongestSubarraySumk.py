class Solution:
    def lenOfLongestSubarr(self, arr, k):  
        # code here
        
        arr_len = 0
        for _ in arr:
            arr_len += 1
            
        if sum(arr) == k:
            return arr_len
            
        preSum = {}
        
        max_len = 0
        cur_sum = 0
        for i in range(arr_len):
            cur_sum += arr[i]
            rem = cur_sum - k
            if rem == 0:
                max_len = max(max_len, i + 1)
                # if there is no remainder then the subarray is from 0 to ith index
            elif preSum.get(rem, None) != None:
                max_len = max(max_len, i - preSum[rem]) 
                # subtracting subarray having the remainder value from the complete 
                # sub array which runs from 0 to ith index
                
            preSum.setdefault(cur_sum, i)
            
        return max_len
    
print(Solution().lenOfLongestSubarr([10, 5, 2, 7, 1, 9], 15)) # 4