from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        max_, nums = 2**31, set(nums)
        for i in range(1, max_):
            if i not in nums:
                return i

        return max_
