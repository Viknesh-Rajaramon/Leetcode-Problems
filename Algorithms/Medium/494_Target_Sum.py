from imports import *

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sum_ = sum(nums)
        if sum_ < target or target < -sum_:
            return 0
        
        n = len(nums)
        dp = [[-inf] * (2*sum_ + 1) for _ in range(n)]
        
        def dfs(curr_sum: int, i: int):
            if i == n:
                return 1 if curr_sum == target else 0
            
            if dp[i][curr_sum + sum_] != -inf:
                return dp[i][curr_sum + sum_]
                
            dp[i][curr_sum + sum_] = dfs(curr_sum + nums[i], i + 1) + dfs(curr_sum - nums[i], i + 1)
            return dp[i][curr_sum + sum_]
        
        return dfs(0, 0)
