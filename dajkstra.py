
#leetcode 743

import heapq

def dijkstra(n: int, edges: list[list[int]], start: int) -> dict:
    parent=[]
    # 1. 인접 리스트로 그래프 구성: u -> (v, weight)
    graph = {i: [] for i in range(1, n + 1)}
    for u, v, w in edges:
        graph[u].append((v, w))
        
    # 2. 최단 거리 테이블 초기화 (무한대)
    INF = float('inf')
    distances = {i: INF for i in range(1, n + 1)}
    distances[start] = 0
    
    # 3. 우선순위 큐 초기화: (현재까지의 누적 비용, 현재 노드)
    # 파이썬 heapq는 튜플의 첫 번째 원소를 기준으로 최소 힙을 구성함
    pq = [(0, start)]
    
    
    while pq:
        cur_dist,cur_node=heapq.heappop(pq)
        
        
        
        if cur_dist>distances[cur_node]:
            #if popm distance longer than current distance
            continue
        
        
        for next_node,weight in graph[cur_node]:
            cost=cur_dist+weight
            
            
            if cost<distances[next_node]:
                distances[next_node]=cost
                parent[next_node]=cur_node#다음노드는 이전노드를 커쳐왔닥도 갱신
                
                heapq.heappush(pq,next_node)
        return distances
    
def get_path(target,parent):
    
    path=[]
    curr=target
    
    while curr is not None:
        path.append(curr)
        curr=parent[curr]
    return  path[::-1]
    # 역ㅊ푸적 거쳐간 경로 출력휴ㅏ기
             
    