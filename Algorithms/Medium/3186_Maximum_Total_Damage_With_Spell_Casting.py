from imports import *

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        counts = Counter(power)
        keys = [0, 0, 0] + sorted(counts.keys())
        n = len(keys)
        dp = [0] * n
        for i in range(3, n):
            curr = counts[keys[i]] * keys[i]
            if keys[i] - keys[i-1] > 2:
                dp[i] = dp[i-1] + curr
            elif keys[i] - keys[i-2] > 2:
                dp[i] = max(dp[i-1], dp[i-2] + curr)
            else:
                dp[i] = max(dp[i-1], dp[i-3] + curr)

        return dp[-1]
