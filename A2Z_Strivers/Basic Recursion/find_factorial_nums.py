# User function Template for python3

class Solution:
    def factorialNumbers(self, n):
        # code here 
        # if n == 1:
        #     return [1]
        # result = []
        # result.extend(self.factorialNumbers(n-1))
        # i = 2
        # if n % i == 0:
        #     temp = n
        #     while n > 1:
        #         n /= i
        #         i += 1
        #     if n == 1:
        #         result.append(temp)
        # # return sorted(result)
        # return result

    # Non recursive solution
        # result = [1]
        # prod = 1
        # for i in range(2,n+1):
        #     prod *= i
        #     if prod <= n:
        #         result.append(prod)
        # return result
        result = [1]
        prod = 1
        i = 2
        # limit = n
        # if n >= 9: 
        # if n < 9, then (sq root of n)! doesn't produce all factorial numbers less than 9
            # limit = int(limit ** 0.5)
        
        while i < n+1:
        # while i < limit:
            prod *= i
            if prod > n:
                break
            result.append(prod)
            i += 1
        return result

# { 
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    # t = int(input())
    t = 1
    for _ in range(t):
        # N = int(input())
        N = 5000000000
        ob = Solution()
        ans = ob.factorialNumbers(N)
        for i in ans:
            print(i, end=" ") 
        print() 
        print("~")