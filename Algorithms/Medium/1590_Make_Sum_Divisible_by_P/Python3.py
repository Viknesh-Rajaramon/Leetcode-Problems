from typing import List
from math import inf

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        target = sum(nums) % p
        if target == 0:
            return 0
        
        mod_map, curr_sum, result = {0: -1}, 0, inf
        for i, num in enumerate(nums):
            curr_sum = (curr_sum + num) % p
            needed = (curr_sum - target + p) % p
            if needed in mod_map:
                result = min(result, i - mod_map[needed])
            
            mod_map[curr_sum] = i
        
        return -1 if result == len(nums) else result
