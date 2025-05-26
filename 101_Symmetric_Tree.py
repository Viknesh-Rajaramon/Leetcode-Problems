from imports import *

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(node_1: Optional[TreeNode], node_2: Optional[TreeNode]) -> bool:
            if not node_1 and not node_2:
                return True
            
            if not node_1 or not node_2:
                return False
            
            return node_1.val == node_2.val and isMirror(node_1.left, node_2.right) and isMirror(node_1.right, node_2.left)
        
        return isMirror(root.left, root.right)
