from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        result = 0
        def dfs(node: Optional[TreeNode], num: int) -> None:
            num <<= 1
            num += node.val

            if not node.left and not node.right:
                nonlocal result
                result += num
                return
            
            if node.left:
                dfs(node.left, num)

            if node.right:
                dfs(node.right, num)

        dfs(root, 0)
        return result
