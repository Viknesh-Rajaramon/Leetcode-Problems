from typing import List
from math import inf

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        m, n = len(nums2), len(nums1)
        if n < m:
            return self.maxScore(nums2, nums1, k)
        
        dp = [[-inf] * (k+1) for _ in range(m+1)]
        for j in range(m+1):
            dp[j][0] = 0
        
        for i in range(n-1, -1, -1):
            next_dp = [[-inf] * (k+1) for _ in range(m+1)]
            for j in range(m+1):
                next_dp[j][0] = 0
            
            for j in range(m-1, -1, -1):
                for p in range(1, k+1):
                    next_dp[j][p] = max(next_dp[j+1][p], dp[j+1][p], dp[j][p], dp[j+1][p-1] + nums1[i]*nums2[j])

            dp = next_dp
        
        return dp[0][k]
