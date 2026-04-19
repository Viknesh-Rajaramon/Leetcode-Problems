from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        subtree_sums = []
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            sum_ = dfs(node.left) + dfs(node.right) + node.val
            subtree_sums.append(sum_)
            return sum_
        
        total_sum = dfs(root)
        return max((total_sum-s)*s for s in subtree_sums) % (10**9+7)
