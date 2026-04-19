from typing import List

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        n, m = len(nums1), len(nums2)
        i, j = 0, 0

        arr = []
        while i < n and j < m:
            if nums1[i][0] == nums2[j][0]:
                arr.append([nums1[i][0], nums1[i][1]+nums2[j][1]])
                i += 1
                j += 1
            elif nums1[i][0] < nums2[j][0]:
                arr.append(nums1[i])
                i += 1
            else:
                arr.append(nums2[j])
                j += 1
        
        while i < n:
            arr.append(nums1[i])
            i += 1
        
        while j < m:
            arr.append(nums2[j])
            j += 1
        
        return arr
