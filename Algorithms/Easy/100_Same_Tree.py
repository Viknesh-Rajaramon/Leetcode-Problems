from imports import *
        
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def inOrderTraversal(root):
            if root is None:
                return [None]
            
            return [root.val] + inOrderTraversal(root.left) + inOrderTraversal(root.right)
        
        return inOrderTraversal(p) == inOrderTraversal(q)
