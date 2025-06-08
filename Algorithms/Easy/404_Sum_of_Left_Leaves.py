from imports import *

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], is_left: bool) -> int:
            if not node:
                return 0
            
            if not node.left and not node.right and is_left:
                return node.val
            
            return dfs(node.left, True) + dfs(node.right, False)

        return dfs(root, False)
