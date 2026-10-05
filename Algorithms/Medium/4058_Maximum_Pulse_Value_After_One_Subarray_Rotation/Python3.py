from typing import List
from math import inf

class Solution:
    def maxValue(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        result, even, odd, sum_ = inf, nums[0], 0, nums[0]
        for i in range(1, n):
            if i%2 == 0:
                sum_ += nums[i]
                even = max(even, sum_)
                result = min(result, sum_ - even)
            else:
                sum_ -= nums[i]
                odd = max(odd, sum_)
                result = min(result, sum_ - odd)
        
        return sum_ - 2*result
