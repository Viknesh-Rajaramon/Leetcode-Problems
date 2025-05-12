from imports import *

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        left_nodes = self.postorderTraversal(root.left)
        right_nodes = self.postorderTraversal(root.right)

        return left_nodes + right_nodes + [root.val]
