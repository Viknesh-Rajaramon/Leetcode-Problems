from typing import List
from math import inf

class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        prev, prev_streak, curr_streak = -inf, 0, 0
        for num in nums:
            if num > prev:
                curr_streak += 1
            else:
                prev_streak = curr_streak
                curr_streak = 1
            
            if curr_streak >= 2*k or (prev_streak >= k and curr_streak >= k):
                return True

            prev = num
        
        return False
