class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        # Recursive solution
        # return self.fib(n-1) + self.fib(n-2)
        i = 0
        j = 1
        k = 1
        count = 1
        while count < n:
            k = i + j
            i = j
            j = k
            count += 1
        
        return k
    
print(Solution().fib(2))