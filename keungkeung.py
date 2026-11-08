
# Definition for a Node.
from collections import deque

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

#같은 레벨을 다 돌앙ㅆ으면 # 추가  엔큐 디큐 후 # list에 #도 같이 추가 
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None 
        
        dq=deque([root])
       
        while dq:
            prev=None   
            size=len(dq)
            for i in range(size):
                curr=dq.popleft()


                if prev:
                   prev.next=curr
                prev=curr
            

                if curr.left:
                   dq.append(curr.left)
                if curr.right:
                   dq.append(curr.right)
        return root
            

#retunr 반환 이유 root 리턴을 하면 root 부터 ㄱ쭉 자식 노드까지 나와서



    
        