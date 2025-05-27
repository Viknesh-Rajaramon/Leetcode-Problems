from imports import *

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node: Optional[TreeNode], curr_sum: int) -> bool:
            if not node.left and not node.right:
                return curr_sum + node.val == targetSum
            
            if node.left and dfs(node.left, curr_sum + node.val):
                return True
            
            if node.right and dfs(node.right, curr_sum + node.val):
                return True
            
            return False
        
        return dfs(root, 0) if root else False
