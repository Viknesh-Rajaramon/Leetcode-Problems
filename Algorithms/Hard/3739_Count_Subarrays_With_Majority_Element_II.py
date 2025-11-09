from imports import *

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        sl, count, result = SortedList([0]), 0, 0
        for num in nums:
            if num == target:
                count += 1
            else:
                count -= 1
            
            result += sl.bisect_left(count)
            sl.add(count)

        return result
