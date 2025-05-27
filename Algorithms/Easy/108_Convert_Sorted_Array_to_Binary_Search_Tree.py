from imports import *

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        
        mid = len(nums) // 2
        
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[ : mid])
        root.right = self.sortedArrayToBST(nums[mid + 1 : ])

        return root
