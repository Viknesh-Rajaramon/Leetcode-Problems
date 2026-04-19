from typing import List
from math import inf

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        n = len(coins)
        
        dp = [inf] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            j = 0
            while j < n and i >= coins[j]:
                dp[i] = min(dp[i], dp[i - coins[j]])
                j += 1
            
            dp[i] += 1
        
        return dp[amount] if dp[amount] != inf else -1
