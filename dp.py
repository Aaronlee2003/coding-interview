class Solution:
2    def uniquePaths(self, m: int, n: int) -> int:
3        dp=[[1 for _ in range(n)] for _ in range(m)]. #n개의 열이 m개 존재

4
5
6
7        for i in range(1,m):
8            for j in range(1,n):
9                dp[i][j]=dp[i-1][j]+dp[i][j-1]
10        return dp[m-1][n-1]

