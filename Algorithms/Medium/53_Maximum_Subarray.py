from imports import *

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum, cur_sum = -inf, 0
        for i in range(len(nums)):
            cur_sum = cur_sum+nums[i]
            max_sum = max(max_sum, cur_sum)
            if cur_sum < 0:
                cur_sum = 0

        return max_sum
