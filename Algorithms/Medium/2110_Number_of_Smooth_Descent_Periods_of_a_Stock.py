from imports import *

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        result, size = 0, 1
        for prev, price in pairwise(prices):
            if prev - price != 1:
                result += (size * (size+1)) // 2
                size = 0
            
            size += 1

        result += (size * (size+1)) // 2
        return result
