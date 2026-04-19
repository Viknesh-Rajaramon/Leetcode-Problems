from typing import List
from collections import Counter

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pair_count, r = 0, -1
        
        count = Counter()
        result = 0
        for l in range(n):
            while pair_count < k and r+1 < n:
                r += 1
                pair_count += count[nums[r]]
                count[nums[r]] += 1

            if pair_count >= k:
                result += n-r
            
            if r == n:
                break

            count[nums[l]] -= 1
            pair_count -= count[nums[l]]

        return result
