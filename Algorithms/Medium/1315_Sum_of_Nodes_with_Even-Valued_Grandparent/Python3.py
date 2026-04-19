from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        def dfs(child: Optional[TreeNode], isParentEven: bool, isGrandparentEven: bool) -> int:
            if not child:
                return 0
            
            total = 0
            if isGrandparentEven:
                total += child.val

            total += dfs(child.left, child.val % 2 == 0, isParentEven)
            total += dfs(child.right, child.val % 2 == 0, isParentEven)

            return total
        
        return dfs(root, False, False)
