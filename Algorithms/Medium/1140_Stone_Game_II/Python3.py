from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        dp, suffix = [[0] * (n+1) for _ in range(n)], [0] * n
        suffix[-1] = piles[-1]
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] + piles[i]
        
        for i in range(n-1, -1, -1):
            for j in range(1, n+1):
                if i+2*j >= n:
                    dp[i][j] = suffix[i]
                else:
                    for k in range(1, 2*j+1):
                        dp[i][j] = max(dp[i][j], suffix[i] - dp[i+k][max(j, k)])

        return dp[0][1]
