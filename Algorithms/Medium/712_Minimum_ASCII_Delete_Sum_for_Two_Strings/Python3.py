class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n = len(s2)
        dp = [0] * (n+1)
        for i in range(len(s1)):
            new_dp = [0] * (n+1)
            for j in range(n):
                if s1[i] == s2[j]:
                    new_dp[j+1] = dp[j] + ord(s1[i])*2
                else:
                    new_dp[j+1] = max(new_dp[j], dp[j+1])
            
            dp = new_dp
        
        return sum(ord(c) for c in s1) + sum(ord(c) for c in s2) - dp[-1]
