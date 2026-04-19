from typing import List
from math import inf

class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        n = len(coins[0])
        dp = [[-inf] * 3 for _ in range(n+1)]
        dp[1] = [0] * 3
        
        for row in coins:
            for j, coin in enumerate(row):
                dp[j+1][2] = max(dp[j][2] + coin, dp[j+1][2] + coin, dp[j][1], dp[j+1][1])
                dp[j+1][1] = max(dp[j][1] + coin, dp[j+1][1] + coin, dp[j][0], dp[j+1][0])
                dp[j+1][0] = max(dp[j][0], dp[j+1][0]) + coin

        return dp[n][2]
