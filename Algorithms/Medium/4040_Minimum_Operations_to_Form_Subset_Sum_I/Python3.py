from math import inf

class Solution:
    def minOperations(self, nums: list[int], sum: int) -> int:
        dp = [inf] * (sum+1)
        dp[0] = 0
        for num in nums:
            new_dp = dp[ : ]
            n, count = num, 0
            while n:
                for i in range(sum, n-1, -1):
                    new_dp[i] = min(new_dp[i], dp[i-n] + count)
                
                count += 1
                n >>= 1
            
            n, count = num << 1, 1
            while n <= sum:
                for i in range(sum, n-1, -1):
                    new_dp[i] = min(new_dp[i], dp[i-n] + count)
                
                count += 1
                n <<= 1
            
            dp = new_dp

        return -1 if dp[-1] == inf else dp[-1]
