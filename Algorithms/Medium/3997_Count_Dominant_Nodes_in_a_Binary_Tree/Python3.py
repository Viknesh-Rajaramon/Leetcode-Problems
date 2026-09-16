# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countDominantNodes(self, root: TreeNode | None) -> int:
        result = 0
        def postorder(node: TreeNode | None) -> int:
            if not node:
                return 0
            
            left_max = postorder(node.left)
            right_max = postorder(node.right)
            if node.val >= left_max and node.val >= right_max:
                nonlocal result
                result += 1
                return node.val
            
            return max(left_max, right_max)

        postorder(root)
        return result
