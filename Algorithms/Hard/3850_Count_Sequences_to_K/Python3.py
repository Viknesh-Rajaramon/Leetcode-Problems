from typing import List

class Solution:
    def countSequences(self, nums: List[int], k: int) -> int:
        memo, n = {}, len(nums)
        def dp(val: int, i: int) -> int:
            if round(val, 10) == k and i == n:
                return 1
            
            if i >= n:
                return 0
            
            if (val, i) in memo:
                return memo[(val, i)]
            
            memo[(val, i)] = dp(val, i+1) + dp(val*nums[i], i+1) + dp(val/nums[i], i+1)
            return memo[(val, i)]

        return dp(1, 0)
