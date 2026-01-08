from typing import List
from math import inf

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums2)
        best = [-inf] * (n+1)
        for num1 in nums1:
            nxt = [-inf] * (n+1)
            for j, num2 in enumerate(nums2):
                use = num1 * num2
                nxt[j+1] = max(use, best[j]+use, best[j+1], nxt[j])

            best = nxt
        
        return best[-1]
