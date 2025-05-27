from imports import *

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        result = 0
        max_index, min_index, l = -1, -1, 0

        for r, num in enumerate(nums):
            if not (minK < num < maxK):
                l = r + 1
                continue

            if num == maxK:
                max_index = r

            if num == minK:
                min_index = r
            
            result += max(0, min(min_index, max_index) - l + 1)

        return result
