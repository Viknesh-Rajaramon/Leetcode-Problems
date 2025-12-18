from typing import List
from math import inf

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans, pi = 0, inf
        for p in prices:
            ans, pi = max(ans, p - pi), min(p, pi)
        
        return ans
