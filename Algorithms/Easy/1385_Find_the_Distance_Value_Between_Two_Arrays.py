from imports import *

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()

        result = 0
        for num in arr1:
            index = bisect_left(arr2, num - d)
            if index == len(arr2) or arr2[index] > num + d:
                result += 1

        return result
