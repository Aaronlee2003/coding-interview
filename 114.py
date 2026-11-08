class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.prev = None
    def flatten(self, root: TreeNode | None) -> None:
    
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        self.flatten(root.right)
        self.flatten(root.left)
        root.right = self.prev  # 내 오른쪽에 직전 노드를 연결
        root.left = None        # 왼쪽 가지는 제거
        self.prev = root        # 이제 내가 다음 노드의 '직전 노드'가 됨#꺼주로 돌아야 삽입 가