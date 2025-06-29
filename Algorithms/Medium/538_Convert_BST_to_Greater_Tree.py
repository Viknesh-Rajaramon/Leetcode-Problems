from imports import *

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node: Optional[TreeNode], curr_sum) -> int:
            if not node:
                return curr_sum
            
            right_sum = dfs(node.right, curr_sum)
            node.val += right_sum
            left_sum = dfs(node.left, node.val)
            
            return left_sum

        dfs(root, 0)
        return root
