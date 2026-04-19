from typing import List
from collections import Counter

class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        counter1 = Counter(nums1)
        sum1 = sum(nums1) + counter1[0]

        counter2 = Counter(nums2)
        sum2 = sum(nums2) + counter2[0]

        if sum1 == sum2:
            return sum1
        elif sum1 < sum2:
            if counter1[0] != 0:
                return sum2
            else:
                return -1
        else:
            if counter2[0] != 0:
                return sum1
            else:
                return -1
