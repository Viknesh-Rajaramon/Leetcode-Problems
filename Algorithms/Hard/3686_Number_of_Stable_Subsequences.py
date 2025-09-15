from imports import *

class Solution:
    def countStableSubsequences(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        o1 = o2 = e1 = e2 = 0
        for num in nums:
            if num % 2:
                o2 = (o2 + o1) % mod
                o1 = (o1 + e1 + e2 + 1) % mod
            else:
                e2 = (e2 + e1) % mod
                e1 = (e1 + o1 + o2 + 1) % mod

        return (o1 + o2 + e1 + e2) % mod
