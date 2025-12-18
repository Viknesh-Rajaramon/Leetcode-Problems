from typing import Optional, List
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        depth_nodes = defaultdict(list)
        
        def dfs(node: Optional[TreeNode], depth: int) -> None:
            if not node:
                return
            
            depth_nodes[depth].append(node.val)
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)

        dfs(root, 0)

        result = [0] * len(depth_nodes)
        for depth, values in depth_nodes.items():
            result[depth] = sum(values) / len(values)
        
        return result
