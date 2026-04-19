from typing import Optional, List
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        depth_nodes = defaultdict(list)
        def inorder_traversal(node: Optional[TreeNode], depth: int):
            if node is None:
                return

            depth_nodes[depth].append(node.val)
            inorder_traversal(node.left, depth+1)
            inorder_traversal(node.right, depth+1)
            return

        inorder_traversal(root, 0)

        def minimum_ops(nums: List[int]) -> int:
            n = len(nums)
            sorted_nums = sorted(nums)
            val_idx_map = {val: idx for idx, val in enumerate(sorted_nums)}
            visited = [False] * n

            result = 0
            for i in range(n):
                if visited[i] or val_idx_map[nums[i]] == i:
                    continue

                cycle_size = 0
                j = i
                while not visited[j]:
                    visited[j] = True
                    j = val_idx_map[nums[j]]
                    cycle_size += 1

                if cycle_size > 1:
                    result += cycle_size - 1

            return result
        
        return sum(minimum_ops(nums) for nums in depth_nodes.values())
