from math import inf

class Solution:
    def minimumDistance(self, word: str) -> int:
        def get_distance(p1, p2):
            return abs(p1//6 - p2//6) + abs(p1%6 - p2%6)
        
        n = len(word)
        dp = [[0] * 26] + [[inf] * 26 for _ in range(n-1)]
        for i in range(n-1):
            curr, prev = ord(word[i+1]) - 65, ord(word[i]) - 65
            d = get_distance(prev, curr)
            for j in range(26):
                dp[i+1][j] = min(dp[i+1][j], dp[i][j] + d)
                if prev == j:
                    for k in range(26):
                        dp[i+1][j] = min(dp[i+1][j], dp[i][k] + get_distance(k, curr))

        return min(dp[n-1])
