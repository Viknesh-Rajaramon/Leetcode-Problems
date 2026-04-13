from typing import List

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        result = len(nums)
        for i, num in enumerate(nums):
            if num == target:
                result = min(result, abs(i-start))

        return result
