from typing import List
from math import inf
from collections import defaultdict

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        indices = defaultdict(list)
        for i, num in enumerate(nums):
            indices[num].append(i)
        
        result = inf
        for num, idx in indices.items():
            for i in range(2, len(idx)):
                result = min(result, 2*(idx[i] - idx[i-2]))

        return result if result != inf else -1
