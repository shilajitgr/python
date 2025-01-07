import json


class Solution:
    def solve(self, A, B):
        
        preceeding_xor = {0:1,}
        xor = 0
        total = 0
        for _, val in enumerate(A):
            xor ^= val
            find = xor ^ B
            if preceeding_xor.get(find, -1) > 0:
                total += preceeding_xor[find]
            
            preceeding_xor[xor] = preceeding_xor.setdefault(xor, 0) + 1
        
        return total
            
            
obj = Solution()
A = [ 4, 2, 2, 6, 4 ]
B = 6
A = [ 4, 2, 2, 6, 4, 6, 3, 5, 4, 2]
B = 6
print(obj.solve(A, B))
A = [ 5, 6, 7, 8, 9 ]
B = 5
A = [ 25, 79, 59, 63, 65, 6, 46, 82, 28, 62 ]
B = 94


# 1 0 0 <- 4
# 0 1 0 <- 2
#=1 1 0 = 6
# 0 1 0 <- 2
#=1 0 0 = 4
# 1 1 0 <- 6
#=0 1 0 = 2
# 1 0 0 <- 4
#=1 1 0 = 6