from typing import List

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        m, n, i = len(nums1), len(nums2), 0
        for j in range(n):
            if nums1[i] > nums2[j]:
                i += 1
                if i >= m:
                    break

        return max(0, j-i)
