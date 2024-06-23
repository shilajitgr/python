# optimal solution - https://takeuforward.org/data-structure/calculate-the-power-of-a-number-binary-exponentiation/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if x == 0:
            return 0
        
        if n == 0:
            return 1
        
        pow_negative = False
        if n < 0:
            pow_negative = True
            n *= -1
        val_negative = False
        if x < 0:
            val_negative = True
            x *= -1
        
        integer = x // 1
        fraction = x - integer
        int_sum = x
        upper_limit = 10**4
        lower_limit = -1*upper_limit
        exp_limit = 10**10
        if fraction < 1/exp_limit:
            fraction = 0
            x = integer
        for _ in range(2, n+1):
            int_sum = x*integer
            int_sum += x*fraction
            x = int_sum
            # if not lower_limit <= x <= upper_limit:
            #     break
            if x <= 1/exp_limit:
                break
            
        if val_negative:
            if n % 2 != 0:
                int_sum *= -1
                
        if pow_negative:
            int_sum = 1/int_sum
            
        return int_sum
    
    
obj = Solution()

print(obj.myPow(1.0000000000001, -2147483648))
    

