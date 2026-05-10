from typing import List

class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [-1] * n
        dp[n-1] = 0
        for i in range(n-2, -1, -1):
            max_j = 0
            for j in range(i+1, n):
                if dp[j] >= max_j and abs(nums[j] - nums[i]) <= target:
                    max_j, dp[i] = dp[j], dp[j] + 1

        return dp[0]
