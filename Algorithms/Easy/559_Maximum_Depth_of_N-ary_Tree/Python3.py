from typing import Optional, List

class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        if not root.children:
            return 1
        
        depth = 0
        for child in root.children:
            depth = max(depth, self.maxDepth(child))

        return depth + 1
