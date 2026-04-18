from typing import List
from math import inf

class Solution:
    def minPartitionScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        prefix_sum = [0] * (n+1)
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]
        
        dp = [0] + [inf] * n
        for p in range(k):
            new_dp, min_i = [inf] * (n+1), p
            for j in range(p+1, n+1):
                for i in range(min_i, j):
                    curr = prefix_sum[j] - prefix_sum[i]
                    cost = dp[i] + curr * (curr+1) // 2
                    if cost < new_dp[j]:
                        new_dp[j] = cost
                        min_i = i
            
            dp = new_dp

        return dp[n]
