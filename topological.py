from collections import deque



def topological_sort(v,edge):
    indegree=[0]*(v+1)#들어오는 노드 가리킴
    
    graph=[[] for _ in range(v+1)]# 나가는 간선 가리킴
    
    #간선정보 등록과 진입 차수 등록
    for u,to_node in edge:
        graph[u].appned(to_node)
        indegree[to_node]+=1
    #들어오는노드 추가
    
    #진입 차수가 0인노드를 큐에 추기ㅏ
    
    # 3. 진입차수가 0인 노드를 큐에 삽입
    queue = deque([i for i in range(1, v + 1) if indegree[i] == 0])
    result = []
    # results는 결과를 정렬을 저장한 배열
    
    while queue:
        now=queue.popleft()
        result.append(now)#등록된 시0인 차수를 집어넘
        
        for next  in graph[now]:
            indegree[next]-=1
            if indegree[next]==0:
                queue.append(next)
                
                
                
    if len(result)<v:
        return False
    
    
    return result
        