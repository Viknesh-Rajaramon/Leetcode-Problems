from imports import *

class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n, half = len(prices), k//2
        
        max_profit = 0
        for i in range(n):
            max_profit += prices[i] * strategy[i]

        mod_profit = max_profit
        for i in range(n):
            if i-k >= 0:
                mod_profit += prices[i-k] * strategy[i-k]
                mod_profit -= prices[i-half]

            if i < half:
                mod_profit -= prices[i] * strategy[i]
            else:
                mod_profit -= prices[i] * strategy[i]
                mod_profit += prices[i]
            
            if i-k >= -1:
                max_profit = max(max_profit, mod_profit)

        return max_profit
