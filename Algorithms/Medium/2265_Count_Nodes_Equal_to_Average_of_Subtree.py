from imports import *

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        result = 0
        def dfs(node: TreeNode) -> Tuple[int, int]:
            nonlocal result
            if not node:
                return 0, 0

            left_sum, left_nodes = dfs(node.left)
            right_sum, right_nodes = dfs(node.right)
            
            sum_ = left_sum + right_sum + node.val
            nodes_ = left_nodes + right_nodes + 1
            if sum_ // nodes_ == node.val:
                result += 1
            
            return sum_, nodes_
        
        dfs(root)
        return result
