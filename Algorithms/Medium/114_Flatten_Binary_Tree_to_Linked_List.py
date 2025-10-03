from imports import *

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        curr = root
        while curr:
            if curr.left:
                pred = curr.left
                while pred.right:
                    pred = pred.right
                
                pred.right = curr.right
                curr.right = curr.left
                curr.left = None

            curr = curr.right
