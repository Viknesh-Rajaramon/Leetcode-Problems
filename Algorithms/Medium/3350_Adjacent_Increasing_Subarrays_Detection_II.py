from typing import List

class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        prev, curr, k = 0, 1, 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                curr += 1
            else:
                k = max(k, curr // 2, min(curr, prev))
                prev = curr
                curr = 1

        return max(k, curr // 2, min(curr, prev))
