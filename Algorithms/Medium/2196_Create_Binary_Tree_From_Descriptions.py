from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}

        for _, child, _ in descriptions:
            if child not in nodes:
                nodes[child] = TreeNode(child)
        
        root = None
        for parent, child, isLeft in descriptions:
            if parent not in nodes:
                root = TreeNode(parent)
                nodes[parent] = root
            
            if isLeft:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]

        return root
