from typing import List
from math import inf

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        min_1, min_2 = inf, inf
        for num in nums[1 : ]:
            if num < min_2:
                min_2 = num
            
            if min_2 < min_1:
                min_1, min_2 = min_2, min_1

        return nums[0] + min_1 + min_2
