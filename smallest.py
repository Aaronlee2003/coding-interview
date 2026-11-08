
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            digit=1
            result=1
            for digit in str(n):
                result*=int(digit)

            if result%t==0:
                return n
            n += 1
        return n
    
                

    