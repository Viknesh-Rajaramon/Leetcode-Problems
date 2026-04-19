from typing import List
from math import inf

class Solution:
    def makeParityAlternating(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 1:
            return [0, 0]
        
        def helper(p: int) -> List[int]:
            max_, min_, ops = -inf, inf, 0
            for i in range(n):
                if nums[i]%2 == p:
                    max_, min_ = max(max_, nums[i]), min(min_, nums[i])
                else:
                    ops += 1
                    max_, min_ = max(max_, nums[i]-1), min(min_, nums[i]+1)

                p ^= 1
            
            return [ops, max(1, max_ - min_)]
        
        x, y = helper(0), helper(1)
        if x[0] < y[0]:
            return x
        elif x[0] > y[0]:
            return y
        
        return [x[0], min(x[1], y[1])]
