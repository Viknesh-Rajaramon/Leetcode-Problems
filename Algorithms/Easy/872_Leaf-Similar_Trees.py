from imports import *

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]) -> List[int]:
            if not node:
                return []
            
            if not node.left and not node.right:
                return [node.val]
            
            return dfs(node.left) + dfs(node.right)
        
        return dfs(root1) == dfs(root2)
