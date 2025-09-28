class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        mod = 10**9 + 7
        
        m = r - l + 1
        dp = [[0] * m for _ in range(n)]
        dp[0] = [1] * m
        for i in range(1, n):
            if i & 1:
                s = sum(dp[i-1]) % mod
                for v in range(m-1, -1, -1):
                    s -= dp[i-1][v]
                    s %= mod
                    dp[i][v] = s
            else:
                s = sum(dp[i-1]) % mod
                for v in range(m):
                    s -= dp[i-1][v]
                    s %= mod
                    dp[i][v] = s
        
        return sum(dp[-1]) * 2 % mod
