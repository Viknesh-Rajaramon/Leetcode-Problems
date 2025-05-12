from imports import *

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1:
            return 0

        dp = [inf] * n
        dp[0] = 0

        i = 0

        while True:
            if i + nums[i] > n-2:
                return dp[i]+1
            
            for j in range(1, nums[i]+1):
                dp[i+j] = min(dp[i+j], dp[i]+1)
            
            i += 1
        
        return dp[n-1]
