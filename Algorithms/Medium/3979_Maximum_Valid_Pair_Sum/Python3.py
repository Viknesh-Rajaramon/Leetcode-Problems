from math import inf

class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        result, left_max = -inf, -inf
        for r in range(k, len(nums)):
            left_max = max(left_max, nums[r-k])
            result = max(result, left_max + nums[r])

        return result
