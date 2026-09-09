from typing import List
from math import inf, ceil

class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        def solve(mul: bool) -> int:
            result, dp_0, dp_1, dp_2 = -inf, -inf, -inf, -inf
            for num in nums:
                if mul:
                    y = num*k
                else:
                    y = num // k if num >= 0 else ceil(num/k)
                
                d_0, d_1, d_2 = max(num, dp_0 + num), max(y, dp_0 + y, dp_1 + y), max(dp_1 + num, dp_2 + num)
                dp_0, dp_1, dp_2 = d_0, d_1, d_2
                result = max(result, dp_1, dp_2)
                
            return result
        
        return max(solve(True), solve(False))
