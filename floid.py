import sys
input = sys.stdin.readline

n = int(input())
v = int(input())
INF = 9999999
graph = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(v) :
    v1, v2, c = map(int, input().split())
    graph[v1][v2] = c


for i in range(1, n+1) :
    graph[i][i] = 0


for  k in range(1,n+1):
     for s  in range(1,n+1):
         for e in range(1,n+1):
             graph[s][e]=min(graph[s][k]+graph[k][e],graph[s][e])

for i in range(1,n+1):
    for j in  range(1,n+1):
        if graph[i][j]==INF:
            print(0)
        else:
            print(graph[i][j])
          