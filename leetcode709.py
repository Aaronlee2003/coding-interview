class ListNode:
    def __init__(self, key: int = -1, val: int = -1, next=None):
        self.key = key
        self.val = val
        self.next = next


class MyHashMap:
    def __init__(self):
        self.size = 1000
        # 각 버킷을 더미 헤드 노드로 초기화
        self.table = [ListNode() for _ in range(self.size)]

    def _hash(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        idx = self._hash(key)
        cur = self.table[idx]

        # 기존 키가 존재하는지 탐색
        while cur.next:
            if cur.next.key == key:
                cur.next.val = value  # 값 갱신
                return
            cur = cur.next

        # 없으면 연결 리스트 끝에 새 노드 추가
        cur.next = ListNode(key, value)

    def get(self, key: int) -> int:
        idx = self._hash(key)
        # 더미 노드 다음 실제 데이터 노드부터 탐색
        cur = self.table[idx].next

        while cur:
            if cur.key == key:
                return cur.val  # key가 아닌 val 반환
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        prev = self.table[idx]
        cur = prev.next

        while cur:
            if cur.key == key:
                prev.next = cur.next  # 노드 삭제
                return
            prev = cur
            cur = cur.next[[[[[]]'''''''[]]]]