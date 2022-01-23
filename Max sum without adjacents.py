"""
Geeks for Geeks contest
"""


# incorrect for large lists

class Solution:
    def findMaxSum(self, arr, n):
        # code here
        if n == 0:
            return 0
        else:
            maxNum = max(arr)
            idx = arr.index(maxNum)
            if idx + 2 > n:
                return maxNum + self.findMaxSum(arr[:(idx - 2)], len(arr[:(idx - 2)]))
            elif 2 <= idx <= n - 2:
                return self.findMaxSum(arr[(idx + 2):], len(arr[(idx + 2):])) + maxNum + self.findMaxSum(
                    arr[:(idx - 1)], len(arr[:(idx - 1)]))
            else:
                return self.findMaxSum(arr[(idx + 2):], len(arr[(idx + 2):])) + maxNum


# 7234
print(Solution().findMaxSum([468, 335, 1, 170, 225, 479, 359, 463, 465, 206, 146, 282, 328, 462, 492, 496, 443, 328,
                             437, 392, 105, 403, 154, 293, 383, 422, 217, 219, 396, 448, 227, 272, 39, 370, 413, 168,
                             300, 36, 395, 204, 312, 323], 42))
