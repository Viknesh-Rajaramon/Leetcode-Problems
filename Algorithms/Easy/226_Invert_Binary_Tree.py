from imports import *

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
