from imports import *

class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        m, n = len(nums1), len(nums2)

        def helper(x1: int, v: int) -> int:
            if x1 > 0:
                return bisect_right(nums2, v // x1)
            elif x1 < 0:
                return n - bisect_left(nums2, -(-v // x1))
            
            return n if v >= 0 else 0
        
        bounds = [nums1[i] * nums2[j] for i in [0, -1] for j in [0, -1]]
        low, high = min(bounds), max(bounds)
        while low <= high:
            mid = (low + high) // 2
            
            count = 0
            for i in range(m):
                count += helper(nums1[i], mid)
            
            if count < k:
                low = mid + 1
            else:
                high = mid - 1
        
        return low
