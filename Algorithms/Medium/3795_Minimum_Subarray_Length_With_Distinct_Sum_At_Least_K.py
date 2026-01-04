from typing import List
from math import inf

class Solution:
    def minLength(self, nums: List[int], k: int) -> int:
        result, l, window_sum, count = inf, 0, 0, {}
        for r in range(len(nums)):
            if nums[r] in count:
                count[nums[r]] += 1
            else:
                window_sum += nums[r]
                count[nums[r]] = 1
            
            while window_sum >= k:
                result = min(result, r-l+1)
                count[nums[l]] -= 1
                if count[nums[l]] == 0:
                    del count[nums[l]]
                    window_sum -= nums[l]

                l += 1

        return result if result != inf else -1
