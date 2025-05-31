from imports import *

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
            
        curr_sum = 0
        if root.val >= low:
            curr_sum += self.rangeSumBST(root.left, low, high)

        if root.val <= high:
            curr_sum += self.rangeSumBST(root.right, low, high)
            
        if low <= root.val <= high:
            curr_sum += root.val

        return curr_sum
