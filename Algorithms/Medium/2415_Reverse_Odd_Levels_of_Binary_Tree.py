from imports import *

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(left: Optional[TreeNode], right: Optional[TreeNode], level: int) -> None:
            if not left or not right:
                return
            
            if level % 2:
                left.val, right.val = right.val, left.val
            
            dfs(left.left, right.right, level+1)
            dfs(left.right, right.left, level+1)

        dfs(root.left, root.right, 1)
        return root
