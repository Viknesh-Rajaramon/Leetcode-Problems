from typing import List
from math import inf

class Solution:
    def maximumProduct(self, nums: List[int], m: int) -> int:
        if m == 1:
            max_, min_ = max(nums), min(nums)
            return max(max_ * max_, min_ * min_)

        result = -inf

        max_, min_ = nums[-1], nums[-1]
        for i in range(len(nums) - m, -1, -1):
            j = i+m-1
            max_ = max(max_, nums[j])
            min_ = min(min_, nums[j])
            result = max(result, max_ * nums[i], min_ * nums[i])

        return result
