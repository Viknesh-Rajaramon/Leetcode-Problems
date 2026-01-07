from typing import Optional, Tuple

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node: Optional[TreeNode]) -> Tuple[int, Optional[TreeNode]]:
            if not node:
                return 0, None
            
            left_d, left_node = dfs(node.left)
            right_d, right_node = dfs(node.right)
            
            if left_d > right_d:
                return left_d+1, left_node
            elif left_d < right_d:
                return right_d+1, right_node
            
            return left_d+1, node
        
        _, node = dfs(root)
        return node
