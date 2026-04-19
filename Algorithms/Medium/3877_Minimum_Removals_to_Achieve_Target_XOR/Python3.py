from typing import List
from math import inf
from functools import lru_cache

class Solution:
    def minRemovals(self, nums: List[int], target: int) -> int:
        n = len(nums)

        @lru_cache(None)
        def dfs(i: int, curr_xor: int) -> int:
            if i >= n:
                return 0 if curr_xor == target else -inf
            
            return max(dfs(i+1, curr_xor^nums[i]) + 1, dfs(i+1, curr_xor))

        result = dfs(0, 0)
        return n - result if result != -inf else -1
