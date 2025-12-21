from typing import List, Tuple

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node: 'TreeNode', val: int) -> Tuple[bool, List[int]]:
            if not node:
                return False, []

            if node.val == val:
                return True, [node]
            
            exists_in_left, left_path = dfs(node.left, val)
            if exists_in_left:
                left_path.append(node)
                return True, left_path
            
            exists_in_right, right_path = dfs(node.right, val)
            if exists_in_right:
                right_path.append(node)
                return True, right_path
            
            return False, []
        
        _, p_path = dfs(root, p.val)
        _, q_path = dfs(root, q.val)

        q_path = set(q_path)
        for node in p_path:
            if node in q_path:
                return node
        
        return root