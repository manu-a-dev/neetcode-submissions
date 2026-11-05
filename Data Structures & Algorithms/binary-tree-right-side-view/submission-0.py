# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        dq = collections.deque([root])
        res = []
        while dq:
            right_side = None
            n = len(dq)
            for i in range(n):
                node = dq.popleft()
                if node:
                    right_side = node
                    dq.append(node.left)
                    dq.append(node.right)
            if right_side:
                res.append(right_side.val)
        return res
        