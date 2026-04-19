from typing import List
from collections import defaultdict

class Solution:
    def countStableSubarrays(self, capacity: List[int]) -> int:
        n, result, prev, map_ = len(capacity), 0, 0, defaultdict(lambda: defaultdict(int))
        for i in range(n):
            result += map_[capacity[i]][prev - capacity[i]]
            prev += capacity[i]
            map_[capacity[i]][prev] += 1
            if i > 0 and capacity[i] == 0 and capacity[i-1] == 0:
                result -= 1
            
        return result
