class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count=0
        n=len(isConnected)
        visited=[False]*n
        
            
        def dfs(city: int):
            visited[city] = True
            # city와 연결된 다른 도시(neighbor)를 탐색
            for neighbor in range(n):
                if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                    dfs(neighbor)
                    
        
        
        for i in range(n):
            for j in range(len(isConnected[0])):
                if not visited[i] and isConnected[i][j]==1:
                    dfs(i)
                    count+=1
        return count           
            
            
            
           