from typing import List
from bisect import bisect_left

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        index = bisect_left(nums, k)
        return index
