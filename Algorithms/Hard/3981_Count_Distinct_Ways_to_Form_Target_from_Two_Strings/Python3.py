class Solution:
    def interleaveCharacters(self, word1: str, word2: str, target: str) -> int:
        m, n, mod = len(word1), len(word2), 10**9+7
        dp = [[0] * (n+1) for _ in range(m+1)]
        dp[m][n] = 1

        for c in target:
            new_dp = [[0] * (n+1) for _ in range(m+1)]
            for i in range(m+1):
                acc = dp[i][n]
                for j in range(n):
                    if word2[j] == c:
                        new_dp[i][j] = (new_dp[i][j] + acc) % mod
                    
                    acc = (acc + dp[i][j]) % mod
            
            for j in range(n+1):
                acc = dp[m][j]
                for i in range(m):
                    if word1[i] == c:
                        new_dp[i][j] = (new_dp[i][j] + acc) % mod
                    
                    acc = (acc + dp[i][j]) % mod
            
            dp = new_dp

        result = 0
        for i in range(m):
            for j in range(n):
                result = (result + dp[i][j]) % mod

        return result
