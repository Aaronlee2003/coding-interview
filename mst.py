class DisjointSet:
    def __init__(self, n: int):
        # 1부터 n번까지의 노드를 처리할 수 있도록 n + 1 크기 할당
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)
        
    def find(self,x:int):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,u:int,v:int)->bool:
        root_u = self.find(u)
        root_v = self.find(v)
    
    
        if root_u == root_v:
            return False
        
        if self.rank[root_u]<=self.rank[root_v]:#hieght of tree
            self.parent[root_u]=root_v
        elif self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
            
        else:
            self.parent[root_v] = root_u
            self.rank[root_u] += 1

        return True
    def kruskal(n: int, edges: list[tuple[int, int, int]]) -> tuple[int, list[tuple[int, int, int]]]:
    # 1. 간선을 가중치 기준 오름차순 정렬
       edges.sort()
       ds=DisjointSet(n)
       mst_cost = 0
       mst_edges = []
       for weight,u,v in edges:
           if ds.union(u,v):
               mst_cost += weight
               mst_edges.append((u, v, weight))
               if len(mst_edges) == n - 1:
                break

       return mst_cost, mst_edges
               
               
       
                 