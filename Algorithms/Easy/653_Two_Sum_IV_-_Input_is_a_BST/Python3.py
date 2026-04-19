from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        nums = []
        
        def dfs(root: Optional[TreeNode]):
            if not root:
                return
            
            nums.append(root.val)
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        
        s = set(nums)
        for i in range(len(nums)):
            if k - nums[i] != nums[i] and k - nums[i] in s:
                return True
            
        return False
