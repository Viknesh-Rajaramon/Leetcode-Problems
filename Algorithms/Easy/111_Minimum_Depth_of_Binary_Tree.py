from imports import *

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return inf
            
            left_depth = dfs(node.left)
            right_depth = dfs(node.right)

            if left_depth == inf and right_depth == inf:
                return 1
            
            return min(left_depth, right_depth) + 1

        return dfs(root) if root else 0
