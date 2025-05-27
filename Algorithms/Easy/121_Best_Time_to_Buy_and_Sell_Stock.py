from imports import *

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        pi = inf

        for p in prices:
            ans = max(ans, p - pi)
            pi = min(p, pi)
        
        return ans
