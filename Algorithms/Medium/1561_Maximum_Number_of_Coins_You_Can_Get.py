from imports import *

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        result = 0
        n = len(piles)
        
        for j in range(n-2, n//3-1, -2):
            result += piles[j]
        
        return result
