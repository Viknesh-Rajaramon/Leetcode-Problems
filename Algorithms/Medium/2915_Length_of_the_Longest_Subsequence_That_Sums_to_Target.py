from imports import *

class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        dp = [-inf] * (target + 1)
        dp[0] = 0

        for i in range(len(nums)):
            for j in range(target, nums[i]-1, -1):
                dp[j] = max(dp[j], dp[j - nums[i]] + 1)
        
        return dp[target] if dp[target] != -inf else -1
