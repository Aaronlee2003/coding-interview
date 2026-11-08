#bellmanford  v-1
def bellman_ford(n: int, edges: list[list[int]], start: int):
    inf=float('inf')
    dist=[inf]*(n+1)
    dist[start]=0
    
    
    
    for i in range(n-1):
        for u,v,w in edges:
            #updated=false
            if dist[u]!=inf and dist[u]+w<dist[v]:
                dist[v]=dist[u]+w
                #updated=true
        # if not updated
        #.  break
                
                
                #다돌고 마지막으로 돌때 갱신이 되면 음수 가중치 존재
    for u,v,w in  edges:
        if dist[u] != inf and dist[u] + w < dist[v]:
            return None
    return dist
            