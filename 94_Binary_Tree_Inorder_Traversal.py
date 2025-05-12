from imports import *

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ptr = root
        stack = []
        arr = list()

        while True:
            if ptr is not None:
                stack.append(ptr)
                ptr = ptr.left
            elif len(stack) != 0:
                ptr = stack.pop()
                arr.append(ptr.val)
                ptr = ptr.right
            else:
                break
        
        return arr
