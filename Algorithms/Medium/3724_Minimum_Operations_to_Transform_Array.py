from imports import *

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        result, v, last = sum(abs(nums1[i] - nums2[i]) for i in range(n)), nums2[-1], inf

        for a, b in zip(nums1, nums2):
            if a <= v <= b or b <= v <= a:
                last = 0
                break
            
            last = min(last, abs(a-v), abs(b-v))
        
        return result + last + 1
