from imports import *

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return bool(root.val)
        
        left = self.evaluateTree(root.left)
        right = self.evaluateTree(root.right)

        return bool(left or right) if root.val == 2 else bool(left and right)
