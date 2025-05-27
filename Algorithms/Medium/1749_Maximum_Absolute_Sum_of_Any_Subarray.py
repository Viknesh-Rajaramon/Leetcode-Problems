from imports import *

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        prefix_sum = list(accumulate(nums, initial=0))
        return max(prefix_sum) - min(prefix_sum)
