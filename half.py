class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        island=0
        near=0


        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    island+=1
                    
                    if i+1<m and grid[i+1][j]==1:
                        near+=1
                    if j+1<n and grid[i][j+1]==1:
                        near+=1
        return (4*island)-(2*near)