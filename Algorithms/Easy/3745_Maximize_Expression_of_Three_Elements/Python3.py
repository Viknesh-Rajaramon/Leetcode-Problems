from typing import List

class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        return nums[0] + nums[1] - nums[-1]
