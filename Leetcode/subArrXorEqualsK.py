class Solution:
    def solve(self, A, B):
        
        sol_list = []
        sol_hash = {}
        xor = 0
        cur_start = 0
        for idx, val in enumerate(A):
            xor = xor ^ val
            
            if val == B:
                sol_hash[idx] = idx
                sol_list.append(A[idx:idx+1])
            
            if xor == 0:
                if sol_hash.get(cur_start-1) > -1:
                    sol_list.append(A[sol_hash.get(cur_start-1):idx+1])
                    sol_hash[idx] = cur_start
                    cur_start = idx + 1
                    xor = 0
                if idx+1 < len(A) and A[idx+1] == B:
                    sol_list.append(A[sol_hash.get(cur_start-1):idx+2])
                    sol_hash[idx+1] = cur_start
            
            if xor == B:
                sol_hash[idx] = cur_start
                sol_list.append(A[cur_start:idx+1])
                cur_start = idx + 1
                xor = 0
                
            print(sol_hash)
            print(sol_list)
        
        return len(sol_list)
            
            
obj = Solution()
A = [ 4, 2, 2, 6, 4 ]
B = 6
print(obj.solve(A, B))