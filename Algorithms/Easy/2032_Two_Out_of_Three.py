from typing import List
from collections import Counter

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        nums1 = Counter(nums1)
        nums2 = Counter(nums2)
        nums3 = Counter(nums3)

        result = set()
        for key in nums1:
            if key in nums2 or key in nums3:
                result.add(key)
        
        for key in nums2:
            if key in nums3:
                result.add(key)
        
        return list(result)
