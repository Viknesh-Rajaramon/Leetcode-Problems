from imports import *

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_ = 0
        max_diff = 0
        result = 0

        for num in nums:
            if max_diff * num > result:
                result = max_diff * num
            if max_ - num > max_diff:
                max_diff = max_ - num
            if num > max_:
                max_ = num
        
        return result
