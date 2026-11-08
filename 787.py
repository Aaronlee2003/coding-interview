from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # 문자열 'inf'가 아니라 수치형 무한대 float('inf')를 사용해야 대소 비교가 가능합니다.
        inf = float('inf')
        dist = [inf] * n
        dist[src] = 0

        for _ in range(k + 1):
            temp = dist[:]  # 이번 턴에 기록할 임시 복사본 생성

            for u, v, w in flights:  # u: 출발지, v: 도착지, w: 가격
                # 아직 도달하지 못한 출발지는 패스
                if dist[u] == inf:
                    continue#한 바퀴 돌면 첫 flight 순회한게 기록
                #

                # 이전 턴(dist) 기준 비용 + 이번 비행편 가격이 현재 temp보다 저렴하면 갱신
                if dist[u] + w < temp[v]:
                    temp[v] = dist[u] + w

            # flights 루프가 완전히 끝난 뒤에 dist를 temp로 교체해야 합니다.
            dist = temp

        return dist[dst] if dist[dst] != inf else -1
                
    #딱 M번만 거쳐야 한다" 또는 "최대 K개의 간선(경유지, 단계, 시간)만 사용해야 한다"처럼 단계 수에 제한이 걸린 최단 거리/경로 문제를
    #배열 복사 생간 직전턴의 상태를 기준으로 해야하기 때문에 이전 상태를 복사
#dist 배열을 저장 최소거리 근데 복사본을 안만들면  0 -> 1 비행기를 타서 dist[1]이 채워집니다. (비행 1회)
#같은 1번째 루프 안에서 바로 뒤이어 1 -> 2 비행기까지 계산해 버려서 dist[2]까지 채워집니다. (비행 2회)
#그러면 dist 2는  2회 거쳐서 간 거리가 됨