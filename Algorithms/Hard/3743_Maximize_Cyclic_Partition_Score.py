from typing import List
from math import inf

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        def solve(arr: List[int]) -> int:
            dp = [[-inf] * 3 for _ in range(k+2)]
            for i in range(1, k+2):
                dp[i][0] = 0
            
            for num in arr:
                for i in range(k+1, 0, -1):
                    dp[i][0] = max(dp[i][0], dp[i][1]+num, dp[i][2]-num)
                    dp[i][1] = max(dp[i][1], dp[i-1][0]-num)
                    dp[i][2] = max(dp[i][2], dp[i-1][0]+num)
            
            return dp[-1][0]

        i = nums.index(min(nums))
        return max(solve(nums[i:] + nums[:i]), solve(nums[i+1:] + nums[:i+1]))
