from typing import List
from heapq import heapify, heappop

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums = list(map(lambda x: x * -1, nums))
        heapify(nums)

        return (heappop(nums)+1) * (heappop(nums)+1)
