from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nums = []
        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                return
                
            dfs(node.left)
            nums.append(node.val)
            dfs(node.right)
        
        dfs(root)
        
        def build_bst(low: int, high: int) -> Optional[TreeNode]:
            if low > high:
                return None
            
            mid = (low+high) // 2
            root = TreeNode(nums[mid])
            root.left = build_bst(low, mid-1)
            root.right = build_bst(mid+1, high)

            return root
        
        return build_bst(0, len(nums)-1)
