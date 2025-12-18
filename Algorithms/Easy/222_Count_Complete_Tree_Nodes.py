from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def get_left_height(node: Optional[TreeNode]) -> int:
            height = 0
            while node:
                height += 1
                node = node.left
            
            return height
        
        def get_right_height(node: Optional[TreeNode]) -> int:
            height = 0
            while node:
                height += 1
                node = node.right
            
            return height
        
        left_height, right_height = get_left_height(root), get_right_height(root)
        if left_height == right_height:
            return 2**left_height - 1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
