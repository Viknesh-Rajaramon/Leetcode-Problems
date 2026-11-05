from typing import List
from bisect import bisect_left

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        result = 0
        for num in arr1:
            idx = bisect_left(arr2, num - d)
            if idx == len(arr2) or arr2[idx] > num + d:
                result += 1

        return result
