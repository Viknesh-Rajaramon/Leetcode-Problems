from imports import *

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        
        i = 1
        while i < len(preorder) and preorder[i] < preorder[0]:
            i += 1
        
        root = TreeNode(preorder[0])
        root.left = self.bstFromPreorder(preorder[1 : i])
        root.right = self.bstFromPreorder(preorder[i : ])

        return root
