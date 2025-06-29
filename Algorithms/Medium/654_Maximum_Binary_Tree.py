from imports import *

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        max_index = 0
        for i in range(1, len(nums)):
            if nums[max_index] < nums[i]:
                max_index = i
        
        node = TreeNode()
        node.val = nums[max_index]
        node.left = self.constructMaximumBinaryTree(nums[ : max_index])
        node.right = self.constructMaximumBinaryTree(nums[max_index+1 : ])
        
        return node
