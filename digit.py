class Solution:
    def countCommas(self, n: int) -> int:
        if n<1000:
            return 0
        
        elif  9999<n<100000:
            return  n-999
        
        
    