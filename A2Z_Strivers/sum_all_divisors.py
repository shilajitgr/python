#User function Template for python3

"""

for any non-negative integer n, if d is a divisor of n then n/d is also a divisor of n.
This property is symmetric about the square root of n by traversing just the first half 
we can avoid redundant iteration and computations improving the efficiency of the 
algorithm.
"""

class Solution:
    def sumOfDivisors(self, n):
        #code here 
        total = 0
    	
        for num in range(1, n+1):
            cur = 1
            divisors = set()
            while cur <= num**0.5:
                if num%cur == 0:
                    divisors.update([cur, num//cur])
                cur += 1
            divisors.add(num)
            total += sum(divisors)
        return total
#{ 
# Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.sumOfDivisors(N)
        print(ans)
        print("~")

# } Driver Code Ends