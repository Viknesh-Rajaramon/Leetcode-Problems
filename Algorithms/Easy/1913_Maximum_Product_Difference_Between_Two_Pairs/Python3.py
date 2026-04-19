from typing import List
from math import inf

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        first_max, second_max = -inf, -inf
        first_min, second_min = inf, inf
        for num in nums:
            if first_max < num:
                second_max, first_max = first_max, num
            elif second_max < num:
                second_max = num
            
            if num < first_min:
                second_min, first_min = first_min, num
            elif num < second_min:
                second_min = num
        
        return first_max * second_max - first_min * second_min
