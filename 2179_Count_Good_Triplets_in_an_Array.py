from imports import *

class Tree:
    def __init__(self, n: int):
        self.tree = [0] * (n+1)
    
    def update(self, index, diff):
        index += 1
        while index < len(self.tree):
            self.tree[index] += diff
            index += index & -index
    
    def query(self, index):
        index += 1
        result = 0
        while index > 0:
            result += self.tree[index]
            index -= index & -index
        
        return result

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)

        pos2 = [0] * n
        for i, num in enumerate(nums2):
            pos2[num] = i
        
        reverse_index_map = [0] * n
        for i, num in enumerate(nums1):
            reverse_index_map[pos2[num]] = i
        
        tree = Tree(n)
        result = 0
        for value in range(n):
            pos = reverse_index_map[value]
            left = tree.query(pos)
            tree.update(pos, 1)
            right = (n - 1 - pos) - (value - left)
            result += right * left
        
        return result
