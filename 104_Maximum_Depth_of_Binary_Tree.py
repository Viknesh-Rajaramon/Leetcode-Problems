from imports import *

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if root is None:
                return 0

            return max(dfs(root.left), dfs(root.right)) + 1

        return dfs(root)
