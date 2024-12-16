#User function Template for python3
class Solution:
    def minJumps(self, arr):
        # code here
        if not arr[0]:
            return -1
        
        path_len = len(arr)
        cur = 0
        jumps = 1
        
        while path_len - cur > 0:
            temp = arr[cur]
            if temp == 0:
                return -1
            if cur + temp >= path_len - 1:
                return jumps
            
            max_val = path_len - (arr[cur+1]+(cur+1)+1)
            temp_cur = cur + 1
            for i in range(cur + 1, cur + temp + 1):
                if path_len - (arr[i] + i + 1) < max_val:
                    temp_cur = i
                    max_val = path_len - (arr[i] + i + 1)
                    
            cur = temp_cur
            jumps += 1
        
        return jumps


#{
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        # n = int(input())
        Arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minJumps(Arr)
        print(ans)
        print("~")
# } Driver Code Ends

# data = "9 10 1 2 3 4 8 0 0 0 0 0 0 0 1"

# arr = [int(x) for x in data.split()]

# for idx, value in enumerate(arr):
#     print(idx, value, len(arr)-(value+idx+1), sep="\t")