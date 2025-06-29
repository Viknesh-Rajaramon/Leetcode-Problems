from imports import *

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
