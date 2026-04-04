from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = sorted(nums1 + nums2)
        n = len(arr)
        return arr[n//2] if n%2 else (arr[n//2] + arr[n//2 - 1]) / 2
