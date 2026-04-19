from typing import List
from math import inf
from functools import lru_cache

class Solution:
    def minXor(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_xor = [0] * (n+1)
        for i in range(n):
            prefix_xor[i+1] = prefix_xor[i] ^ nums[i]
        
        @lru_cache(None)
        def dfs(start: int, cuts_left: int) -> int:
            if cuts_left == 1:
                return prefix_xor[n] ^ prefix_xor[start]

            result = inf
            for end in range(start + 1, n - cuts_left + 2):
                left_xor = prefix_xor[end] ^ prefix_xor[start]
                right_xor = dfs(end, cuts_left - 1)

                result = min(result, max(left_xor, right_xor))

            return result

        return dfs(0, k)
