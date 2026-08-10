from math import sqrt

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n+1)
        for i in range(1, n+1):
            for j in range(int(sqrt(i)), 0, -1):
                if not dp[i - j**2]:
                    dp[i] = True
                    break

        return dp[n]
