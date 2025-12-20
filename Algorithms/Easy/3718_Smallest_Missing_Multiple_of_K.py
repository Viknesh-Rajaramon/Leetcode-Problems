from typing import List

class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        result, nums = k, set(nums)
        while result in nums:
            result += k
        
        return result
