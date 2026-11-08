class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        
        answer=[]
        n=len(nums)
        
        mi=10000000
        
        
        
        
        
        for i in range(n-1,-1,-1):
            mi=min(mi,nums[i])
            answer[i]=mi
            
            
        ma=0
        for i in range(n-1):
            ma=max(ma,nums[i])
            
            if ma-answer[i]<=k:
                return i
                
        return -1
            
            
            