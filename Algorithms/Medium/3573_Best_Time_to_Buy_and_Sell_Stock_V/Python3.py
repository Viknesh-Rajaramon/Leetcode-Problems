from typing import List
from math import inf

class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        k = min(k, len(prices)//2)
        dp, dp_long, dp_short = [-inf] * (k+1), [-inf] * (k+1), [-inf] * (k+1)
        dp[0] = 0
        for price in prices:
            new_dp, new_dp_long, new_dp_short = dp[ : ], dp_long[ : ], dp_short[ : ]
            for t in range(k):
                if dp[t] != -inf:
                    if dp[t] - price > new_dp_long[t]:
                            new_dp_long[t] = dp[t] - price
                    
                    if dp[t] + price > new_dp_short[t]:
                        new_dp_short[t] = dp[t] + price

            for t in range(k):
                if dp_long[t] != -inf and dp_long[t] + price > new_dp[t+1]:
                    new_dp[t+1] = dp_long[t] + price
                
                if dp_short[t] != -inf and dp_short[t] - price > new_dp[t+1]:
                    new_dp[t+1] = dp_short[t] - price

            dp, dp_long, dp_short = new_dp, new_dp_long, new_dp_short
        
        return max(dp)
