from typing import List

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        result, nums = [], set(nums)
        for num in range(min(nums), max(nums)+1):
            if num not in nums:
                result.append(num)

        return result
