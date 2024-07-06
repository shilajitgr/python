# dynamic programming problem

class Solution:
    def countPaths(self, i: int, j: int, n: int, m: int, dp: list[list[int]]) -> int:
        if i == (n - 1) and j == (m - 1):
            return 1
        if i >= n or j >= m:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        else:
            dp[i][j] = self.countPaths(
                i + 1, j, n, m, dp) + self.countPaths(i, j + 1, n, m, dp)
            return dp[i][j]


    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]


        # dp[1][1]=1;
        num = self.countPaths(0, 0, m, n, dp)
        if m == 1 and n == 1:
            return num
        return dp[0][0]
    

obj = Solution()
totalCount = obj.uniquePaths(3, 7)
print("The total number of Unique Paths are", totalCount)
