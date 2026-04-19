from typing import Optional
from math import inf

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        result, queue, max_level_sum, curr_level = 1, [root], -inf, 1
        while queue:
            next_level, level_sum = [], 0
            for node in queue:
                level_sum += node.val
                if node.left:
                    next_level.append(node.left)

                if node.right:
                    next_level.append(node.right)

            if level_sum > max_level_sum:
                max_level_sum = level_sum
                result = curr_level
            
            queue = next_level
            curr_level += 1

        return result
