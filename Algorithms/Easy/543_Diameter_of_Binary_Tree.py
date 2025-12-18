from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0

        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
        
            left_depth = dfs(node.left)
            right_depth = dfs(node.right)

            nonlocal result
            result = max(result, left_depth + right_depth)

            return max(left_depth, right_depth) + 1

        dfs(root)
        return result
