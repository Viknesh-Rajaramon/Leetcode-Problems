from imports import *

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        stack = []
        for i in range(n):
            while stack and prices[i] <= prices[stack[-1]]:
                pos = stack.pop()
                prices[pos] -= prices[i]

            stack.append(i)
        
        return prices
