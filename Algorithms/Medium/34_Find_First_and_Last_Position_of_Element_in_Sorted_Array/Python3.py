from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = bisect_left(nums, target), bisect_right(nums, target)
        return [l, r-1] if l != r else [-1, -1]
