from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def inOrderTraversal(root):
            if root is None:
                return [None]
            
            return [root.val] + inOrderTraversal(root.left) + inOrderTraversal(root.right)
        
        return inOrderTraversal(p) == inOrderTraversal(q)
