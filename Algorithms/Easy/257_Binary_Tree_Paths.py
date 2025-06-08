from imports import *

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
