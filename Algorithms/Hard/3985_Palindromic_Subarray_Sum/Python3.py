from typing import List
from math import inf

class Solution:
    def getSum(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * (n+1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
        
        result, tree, last = -inf, [[0, 1, {}], [-1, 1, {}]], 0
        def walk(node: int, i: int) -> int:
            while i-1-tree[node][0] < 0 or nums[i-1-tree[node][0]] != nums[i]:
                node = tree[node][1]
            
            return node
        
        for i in range(n):
            curr = walk(last, i)
            if nums[i] not in tree[curr][2]:
                link, len_ = walk(tree[curr][1], i), tree[curr][0]+2
                tree.append([len_, 0 if tree[curr][0] == -1 else tree[link][2][nums[i]], {}])
                tree[curr][2][nums[i]] = len(tree)-1
                result = max(result, prefix[i+1] - prefix[i+1-len_])
            
            last = tree[curr][2][nums[i]]

        return result
