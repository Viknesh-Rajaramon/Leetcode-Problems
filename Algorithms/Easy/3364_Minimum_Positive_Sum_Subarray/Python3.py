from typing import List
from math import inf

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        prefix_sum = [0] * (n+1)
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]
        
        result = inf
        for length in range(l, min(r, n)+1):
            for start in range(n-length+1):
                total = prefix_sum[start+length] - prefix_sum[start]
                if total > 0:
                    result = min(result, total)

        return result if result != inf else -1
