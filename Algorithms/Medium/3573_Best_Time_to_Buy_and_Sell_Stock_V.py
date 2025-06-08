from imports import *

class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        dp = [[[-inf] * 3 for _ in range(k+1)] for _ in range(n)]

        for t in range(k+1):
            dp[0][t][0] = 0
            if t > 0:
                dp[0][t][1] = -prices[0]
                dp[0][t][2] = prices[0]
            
        for i in range(1, n):
            for t in range(k+1):
                dp[i][t][0] = dp[i-1][t][0]
                if t <= k:
                    dp[i][t][0] = max(dp[i][t][0], dp[i-1][t][1] + prices[i], dp[i-1][t][2] - prices[i])
                    
                if t > 0:
                    dp[i][t][1] = max(dp[i-1][t][1], dp[i-1][t-1][0] - prices[i])
                    dp[i][t][2] = max(dp[i-1][t][2], dp[i-1][t-1][0] + prices[i])
        
        max_profit = 0
        for t in range(k+1):
            max_profit = max(max_profit, dp[n-1][t][0])
        
        return max_profit
