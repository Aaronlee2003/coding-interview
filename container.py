###  2개의 길이를 비교하며 작은길이는 오른쪽으로 이동 시킨다.높이는 작은것을 높이로 삼음 그래야ㅕ Over 되지 않ㅇ름
#세로의 길이는 이진 탐색으
##그다음의 큰길이의 인덱스와 작은 길이의 인덱스를 빼서 가로를 궇란다
##그다음 높이와 가로를 곱해 넓이를 구함

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        max_water=0
        while left<right:
            width=right-left
            curent_height=min(height[left], height[right])
            area=curent_height*width
            max_water=max(area,max_water)
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        return max_water