from typing import List
from math import inf

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        max_1, max_2, max_3, min_1, min_2 = -inf, -inf, -inf, inf, inf
        for num in nums:
            if num > max_1:
                max_1, max_2, max_3 = num, max_1, max_2
            elif num > max_2:
                max_2, max_3 = num, max_2
            elif num > max_3:
                max_3 = num
            
            if num < min_1:
                min_1, min_2 = num, min_1
            elif num < min_2:
                min_2 = num
        
        return max(max_1 * max_2 * max_3, min_1 * min_2 * max_1)
