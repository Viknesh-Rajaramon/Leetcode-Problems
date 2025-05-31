from imports import *

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
