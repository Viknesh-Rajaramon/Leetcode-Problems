from imports import *

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        dp = [0] * n
        min_index = [-1] * n
        min_index[0] = 0

        for i in range(1, n):
            profit = prices[i] - prices[min_index[i-1]]
            if profit > 0:
                dp[i] = profit + dp[i-1]
                min_index[i] = i
            else:
                dp[i] = dp[i-1]
                min_index[i] = i if prices[i] < prices[min_index[i-1]] else min_index[i-1]

        return dp[n-1]
