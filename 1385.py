class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr1.sort()
        arr2.sort()
        count=0
        
        
        
        for i in range(len(arr1)):
            for j in range(len(arr2)):
                if abs(arr1[i]-arr2[j])<=d:
                    break
            else:
                count+=1
        return count