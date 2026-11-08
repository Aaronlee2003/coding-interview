class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

from collections import deque

#zigzag eqaul bfs  print same level  node include array
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        dq=deque([root])
        answer=[]
        level=0
        left_to_right = True#레벨마다 방향을 뒤집어 줘야 해서 
        while dq:
            level_size = len(dq)
            current_level = []
            
            for _ in range(level_size):
                node = dq.popleft()
                
               
                current_level.append(node.val)
                
               
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            if not left_to_right:
                current_level.reverse()
            left_to_right=not left_to_right

            answer.append(current_level)

        return answer






         
            
                


  


            

        