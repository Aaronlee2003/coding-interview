class Solution:
    def climbStairs(self, n: int) -> int:
        
        
        if n<=2:
            return n
        dp=[0]*(n+1)
        
        dp[1]=1
        dp[2]=2
        
        
        
        
        for i in range(3,n):
            dp[n]=dp[n-1]+dp[n-2]
            
            
        return dp[n]
    
