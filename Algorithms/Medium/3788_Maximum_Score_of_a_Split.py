from typing import List
from math import inf

class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum, suffix_min = [0] * (n-1), [inf] * (n-1)
        prefix_sum[0] = nums[0]
        for i in range(n-2):
            prefix_sum[i+1] = prefix_sum[i] + nums[i+1]

        suffix_min[-1] = nums[-1]
        for i in range(n-3, -1, -1):
            suffix_min[i] = min(nums[i+1], suffix_min[i+1])

        return max(p - s for p, s in zip(prefix_sum, suffix_min))
