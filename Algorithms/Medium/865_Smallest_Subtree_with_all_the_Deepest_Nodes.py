from typing import Optional, Tuple

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node: Optional[TreeNode], depth: int) -> Tuple[Optional[TreeNode], int]:
            if node.left is None and node.right is None:
                return node, depth
            
            left, left_depth = dfs(node.left, depth+1) if node.left is not None else (node, depth)
            right, right_depth = dfs(node.right, depth+1) if node.right is not None else (node, depth)

            if left_depth > right_depth:
                return left, left_depth
            elif left_depth < right_depth:
                return right, right_depth
            
            return node, left_depth
        
        subtree, _ = dfs(root, 0)
        return subtree
