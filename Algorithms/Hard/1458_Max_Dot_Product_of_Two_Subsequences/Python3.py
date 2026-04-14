from typing import List
from math import inf

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums2)
        result = [-inf] * (n+1)
        for num1 in nums1:
            nxt = [-inf] * (n+1)
            for j, num2 in enumerate(nums2):
                use = num1 * num2
                nxt[j+1] = max(use, result[j]+use, result[j+1], nxt[j])

            result = nxt
        
        return result[-1]
