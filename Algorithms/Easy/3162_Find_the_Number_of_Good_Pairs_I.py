from imports import *

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        result = 0

        for i in range(len(nums1)):
            if nums1[i] % k:
                continue
            
            num = nums1[i] // k
            for j in range(len(nums2)):
                if num % nums2[j] == 0:
                    result += 1
        
        return result
