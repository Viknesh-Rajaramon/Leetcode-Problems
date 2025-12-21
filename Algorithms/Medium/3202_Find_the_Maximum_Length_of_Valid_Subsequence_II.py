from typing import List

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [[0] * k for _ in range(k)]
        for curr in nums:
            curr = curr % k
            for prev in range(k):
                dp[prev][curr] = dp[curr][prev] + 1
        
        return max(map(max, dp))
