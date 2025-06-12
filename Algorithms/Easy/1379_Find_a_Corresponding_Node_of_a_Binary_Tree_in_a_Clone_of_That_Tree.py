from imports import *

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(original: TreeNode, cloned: TreeNode):
            if not original:
                return
            
            if original == target:
                return cloned
            
            return dfs(original.left, cloned.left) or dfs(original.right, cloned.right)
        
        return dfs(original, cloned)
