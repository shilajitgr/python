class Solution:
    def leaders(self, arr):
        leaders = [arr[-1]]
        max_val = arr[-1]
        for num in range(len(arr)-2,-1,-1):
            if arr[num] >= max_val:
                leaders.append(arr[num])
                max_val = arr[num]
        
        leaders = leaders[::-1]
        
        return leaders
    
print(Solution().leaders([16, 17, 4, 3, 5, 2])) # [17, 5, 2]
print(Solution().leaders([30, 10, 10, 5])) # [30, 10, 10, 5]
print(Solution().leaders([10, 4, 2, 4, 1])) # [10, 4, 4, 1]
