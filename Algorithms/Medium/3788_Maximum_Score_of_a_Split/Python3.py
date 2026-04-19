from typing import List

class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        prefix_sum, suffix_min = sum(nums[ : -1]), nums[-1]
        result = prefix_sum - suffix_min
        for i in range(len(nums)-2, 0, -1):
            prefix_sum -= nums[i]
            suffix_min = min(suffix_min, nums[i])
            result = max(result, prefix_sum - suffix_min)

        return result
