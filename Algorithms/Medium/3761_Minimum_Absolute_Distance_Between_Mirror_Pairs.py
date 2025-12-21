from typing import List
from math import inf

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        result, idx = inf, {}
        for i, num in enumerate(nums):
            if num in idx and idx[num] != i:
                result = min(result, i - idx[num])
            
            idx[int(str(num)[::-1])] = i
        
        return -1 if result == inf else result
