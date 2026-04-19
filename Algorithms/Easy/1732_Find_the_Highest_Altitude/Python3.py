from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr_sum = 0
        max_val = 0
        for g in gain:
            curr_sum += g
            if curr_sum > max_val:
                max_val = curr_sum
        
        return max_val
