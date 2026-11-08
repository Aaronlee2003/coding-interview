from typing import List


class Solution:

    def remainingMethods(
        self, n: int, k: int, invocations: List[List[int]]
    ) -> List[int]:
     
        graph = [[] for _ in range(n)]
        for u, v in invocations:
            graph[u].append(v)

        suspicious = set()

        def dfs(node):
            suspicious.add(node)
            for neighbor in graph[node]:
                if neighbor not in suspicious:
                    dfs(neighbor)

        dfs(k)

        for u, v in invocations:
            if u not in suspicious and v in suspicious:
                return list(range(n))

        # 4. 검증 통과 시 의심 노드를 제외한 나머지 노드 반환
        return [i for i in range(n) if i not in suspicious]