from typing import List
from math import inf

class Solution:
    def minArraySum(self, nums: List[int], k: int) -> int:
        dp, best = 0, [inf] * k
        best[0] = 0
        prefix = 0

        for num in nums:
            prefix = (prefix + num) % k
            keep = dp + num
            dp = keep if keep < best[prefix] else best[prefix]
            if dp < best[prefix]:
                best[prefix] = dp
            
        return dp
