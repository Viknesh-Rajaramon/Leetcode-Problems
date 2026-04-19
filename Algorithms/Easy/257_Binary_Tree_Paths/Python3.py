from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []

        def dfs(node: Optional[TreeNode], path: List[str]) -> None:
            path.append(str(node.val))
            if not node.left and not node.right:
                result.append("->".join(path))
            else:
                if node.left:
                    dfs(node.left, path)
                if node.right:
                    dfs(node.right, path)
            
            path.pop()

        dfs(root, [])
        return result
