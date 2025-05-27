from imports import *

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]) -> Tuple[bool, int]:
            if not node:
                return True, 0
            
            left_is_balanced, left_depth = dfs(node.left)
            if not left_is_balanced:
                return False, 0
            
            right_is_balanced, right_depth = dfs(node.right)
            if not right_is_balanced:
                return False, 0
            
            depth = max(left_depth, right_depth) + 1
            return max(left_depth, right_depth) - min(left_depth, right_depth) <= 1, depth
        
        is_balanced, _ = dfs(root)
        return is_balanced
