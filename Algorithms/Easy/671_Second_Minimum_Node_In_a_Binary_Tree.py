from imports import *

class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        first_min, second_min = inf, inf

        def dfs(node: Optional[TreeNode]) -> None:
            if not node.left and not node.right:
                nonlocal first_min, second_min
                if node.val < first_min:
                    second_min = first_min
                    first_min = node.val
                elif first_min < node.val < second_min:
                    second_min = node.val

                return
            
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return second_min if second_min != inf else -1
