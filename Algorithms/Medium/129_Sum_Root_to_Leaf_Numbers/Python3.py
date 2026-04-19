from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        nums = []
        def dfs(node: Optional[TreeNode], num: int):
            if not node:
                return

            if not node.left and not node.right:
                nums.append(num*10 + node.val)
                return
            
            dfs(node.left, num*10 + node.val)
            dfs(node.right, num*10 + node.val)

        dfs(root, 0)
        return sum(nums)
