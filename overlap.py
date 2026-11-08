from collections import defaultdict


class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        #0->1 1->0    image 1 밀얶을때 이미지랑 1이랑 비교해서 긑숫자
        
        n=len(img1)
        points1 = [(r, c) for r in range(n) for c in range(n) if img1[r][c] == 1]
        points2 = [(r, c) for r in range(n) for c in range(n) if img2[r][c] == 1]
        if not points1 or not points2:
           return 0
        shift_count = defaultdict(int)
        for r1,c1 in points1:
            for r2,c2 in points2:
                dr=r1-r2
                dc=c1-c2
                
                shift_count[(dr,dr)]+=1
        return max(shift_count.values())
       