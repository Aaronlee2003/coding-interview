class Solution:
    def countCommas(self, n: int) -> int:
        
        answer=0
        threshold=1000
        
        
        while n>=threshold:
            answer=n-threshold+1
            threshold*=1000
            
        return answer
            