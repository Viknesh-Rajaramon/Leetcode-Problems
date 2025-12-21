from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        max_depth, result = 0, 0
        queue = deque([(root, 0)])
        
        while queue:
            node, depth = queue.popleft()
            
            if not node.left and not node.right:
                if depth > max_depth:
                    result = node.val
                    max_depth = depth
                elif depth == max_depth:
                    result += node.val
                
                continue
            
            if node.left:
                queue.append((node.left, depth+1))
            
            if node.right:
                queue.append((node.right, depth+1))
        
        return result
