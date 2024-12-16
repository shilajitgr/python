# https://www.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1

class Solution:
    def maxLen(self, n, arr):
        #Code here
        nums_len = len(arr)

        if sum(arr) == 0:
            return nums_len
        
        tracker = {}
        sumarr = 0
        max = 0
        for i in range(len(arr)):
            sumarr += arr[i]
            if sumarr == 0:
                max = i+1
            else:
                if tracker.get(sumarr,-1) >= 0:
                    if max < i - tracker[sumarr]:
                        max = i - tracker[sumarr]
                else:
                    tracker[sumarr] = i
        print(tracker)
        return max
    
obj = Solution()
arr = [15,-2,2,-8,1,7,10,23]
print(obj.maxLen(len(arr), arr))