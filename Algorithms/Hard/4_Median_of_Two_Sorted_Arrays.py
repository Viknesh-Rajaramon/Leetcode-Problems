from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        total = m + n
        i, j = 0, 0
        
        def solve(mid: int, low_nums1, high_nums1, low_nums2, high_nums2) -> int:
            if low_nums1 > high_nums1:
                return nums2[mid - low_nums1]
            
            if low_nums2 > high_nums2:
                return nums1[mid - low_nums2]
            
            mid_nums1, mid_nums2 = (low_nums1 + high_nums1) // 2, (low_nums2 + high_nums2) // 2
            if mid_nums1 + mid_nums2 < mid:
                if nums1[mid_nums1] > nums2[mid_nums2]:
                    return solve(mid, low_nums1, high_nums1, mid_nums2 + 1, high_nums2)
                else:
                    return solve(mid, mid_nums1 + 1, high_nums1, low_nums2, high_nums2)
            else:
                if nums1[mid_nums1] > nums2[mid_nums2]:
                    return solve(mid, low_nums1, mid_nums1 - 1, low_nums2, high_nums2)
                else:
                    return solve(mid, low_nums1, high_nums1, low_nums2, mid_nums2 - 1)
        
        if total % 2:
            return solve(total // 2, 0, m - 1, 0, n - 1)
        else:
            return (solve(total // 2 - 1, 0, m - 1, 0, n - 1) + solve(total // 2, 0, m - 1, 0, n - 1)) / 2
