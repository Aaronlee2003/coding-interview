from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result={}
        
        
        for num in nums:
            result[num]= result.get(num, 0) + 1
        
        
        
        for k,v in result.items():
            if v==1:
                return k