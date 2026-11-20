from typing import List
from collections import defaultdict

class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        result, dp = 0, defaultdict(int)
        for num in nums:
            dp[num+1], dp[num] = dp[num]+1, dp[num-1]+1
            result = max(result, dp[num+1], dp[num])

        return result
