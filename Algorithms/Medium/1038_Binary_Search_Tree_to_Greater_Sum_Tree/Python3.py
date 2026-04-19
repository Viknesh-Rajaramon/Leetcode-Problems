from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node: Optional[TreeNode], curr_sum) -> int:
            if not node:
                return curr_sum
            
            right_sum = dfs(node.right, curr_sum)
            node.val += right_sum
            left_sum = dfs(node.left, node.val)
            
            return left_sum

        dfs(root, 0)
        return root
