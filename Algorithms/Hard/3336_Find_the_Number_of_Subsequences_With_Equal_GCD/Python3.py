from typing import List
from math import gcd

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        mod, m = 10**9+7, max(nums)
        dp = [[0] * (m+1) for _ in range(m+1)]
        dp[0][0] = 1
        for num in nums:
            new_dp = [[0] * (m+1) for _ in range(m+1)]
            for i in range(m+1):
                div_1 = gcd(i, num)
                for j in range(m+1):
                    if dp[i][j] == 0:
                        continue
                    
                    div_2 = gcd(j, num)
                    new_dp[i][j] = (new_dp[i][j] + dp[i][j]) % mod
                    new_dp[div_1][j] = (new_dp[div_1][j] + dp[i][j]) % mod
                    new_dp[i][div_2] = (new_dp[i][div_2] + dp[i][j]) % mod
            
            dp = new_dp
        
        result = 0
        for i in range(1, m+1):
            result = (result + dp[i][i]) % mod

        return result
