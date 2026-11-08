from collection import deque
def bfs(graph,node,visited):
    queue=deque([node])
    visited[node]=True
    while queue:
        m=queue.popleft()
        print(m,end=" ")
        for i in graph[m]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
                
                
                
def dfs(graph,node,visited):
    visited[node]=True
    print(node,end=" ")
    for i in graph[node]:
         if not visited[i]:
                dfs(graph,i,visited)
                
def stackdfs(graph,node,visited):
    visited=[]
    stack=[node]
    
    while stack:
        m=stack.pop()
        if m not in visited:
            print(m,end=" ")
            visited.append(m)
            for i in graph[m]:
                if i not in visited:
                    stack.append(i)