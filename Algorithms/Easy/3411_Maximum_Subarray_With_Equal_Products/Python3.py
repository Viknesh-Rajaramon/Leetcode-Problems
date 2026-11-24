from typing import List
from math import gcd

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        result, prod, l = 2, 1, 0
        for r in range(len(nums)):
            while gcd(prod, nums[r]) > 1:
                prod //= nums[l]
                l += 1
            
            prod *= nums[r]
            result = max(result, r-l+1)

        return result
