from imports import *

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[n-1] = True

        for i in range(n-2, -1, -1):
            jump = False
            for j in range(1, nums[i]+1):
                if dp[i+j]:
                    jump = True
                    break
                
            dp[i] = jump

        return dp[0]
