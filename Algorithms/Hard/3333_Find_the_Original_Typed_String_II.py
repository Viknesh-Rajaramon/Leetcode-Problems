class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        mod = 10**9 + 7
        
        groups, count = [], 1
        for i in range(1, len(word)):
            if word[i-1] == word[i]:
                count += 1
            else:
                groups.append(count)
                count = 1
        
        groups.append(count)
        
        result = 1
        for f in groups:
            result = result * f % mod
        
        n = len(groups)
        if k <= n:
            return result

        dp = [0] * k
        dp[0] = 1
        for num in groups:
            new_dp = [0] * k
            sum_ = 0

            for j in range(k):
                if j > 0:
                    sum_ = (sum_ + dp[j-1]) % mod
                if j > num:
                    sum_ = (sum_ - dp[j - num - 1] + mod) % mod
                
                new_dp[j] = sum_

            dp = new_dp
        
        invalid = sum(dp[n : k]) % mod
        return (result - invalid + mod) % mod
