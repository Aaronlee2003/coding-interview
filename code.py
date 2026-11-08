class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head: ListNode) -> bool:
    if not head or not head.next:
        return False
    
    slow = head  # 거북이
    fast = head  # 토끼
    
    while fast and fast.next:
        slow = slow.next          # 1칸 이동
        fast = fast.next.next     # 2칸 이동
        
        if slow == fast:          # 사이클 감지
            return True
            
    return False
        